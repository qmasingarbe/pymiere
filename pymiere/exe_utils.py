import os
import sys
import time
import re
from subprocess import check_output, call
from distutils.version import StrictVersion
try:
    import _winreg as wr  # python 2
except:
    import winreg as wr  # python 3

IS_PYTHON_2 = sys.version_info.major == 2


def count_running_exe(exe_name):
    """
    Using tasklist windows command, we can find the number of process running with a specific name
    :param exe_name: (str) exact name of the process (ex : 'pycharm64.exe')
    :return:
    """
    # use tasklist command with filter by name
    call = 'TASKLIST', '/FI', 'imagename eq {}'.format(exe_name)
    if IS_PYTHON_2:
        output = check_output(call)
    else:
        output = check_output(call, text=True)
    # check in last line for process name
    lines = output.strip().splitlines()
    return len([l for l in lines if l.lower().startswith(exe_name.lower())])


def exe_is_running(exe_name):
    """
    See count_running_exe
    :param exe_name: (str) exact name of the process (ex : 'pycharm64.exe')
    :return: (bool) exe is running, (int) pid
    """
    # use tasklist command with filter by name
    call = 'TASKLIST', '/FI', 'imagename eq {}'.format(exe_name)
    if IS_PYTHON_2:
        output = check_output(call)
    else:
        output = check_output(call, text=True)
    # check in last line for process name
    lines = output.strip().splitlines()
    if lines[-1].lower().startswith(exe_name.lower()):
        return True, int(re.findall("   ([0-9]{1,6}) [a-zA-Z]", lines[-1])[0])
    return False, None


def get_installed_softwares_info(name_filter, names=["DisplayVersion", "InstallLocation"]):
    """
    Looking into Uninstall key in Windows registry, we can get some infos about installed software
    :param name_filter: (str) filter software containing this name
    :return: (list of dict) info of software found
    """
    reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
    key = wr.OpenKey(reg, r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall")
    apps_info = list()
    # list all installed apps
    for i in range(wr.QueryInfoKey(key)[0]):
        subkey_name = wr.EnumKey(key,i)
        subkey = wr.OpenKey(key, subkey_name)
        try:
            soft_name = wr.QueryValueEx(subkey, "DisplayName")[0]
        except EnvironmentError:
            continue
        if name_filter.lower() not in soft_name.lower():
            continue
        apps_info.append(dict({n: wr.QueryValueEx(subkey, n)[0] for n in names}, DisplayName=soft_name))
    return apps_info


def get_last_premiere_exe():
    """
    Hopefully compute the path to the exe file for premiere
    :return: (str) path to exe
    """
    premiere_versions = get_installed_softwares_info("adobe premiere pro")
    if not premiere_versions:
        raise OSError("Could not find an Adobe Premiere Pro version installed on this computer")
    # find last installed version
    last_version_num = sorted([StrictVersion(v["DisplayVersion"]) for v in premiere_versions])[-1]
    last_version_info = [v for v in premiere_versions if v["DisplayVersion"] == str(last_version_num)][0]
    # build exe path
    exe_path = last_version_info["InstallLocation"]
    if "Premiere" not in exe_path:
        exe_path = os.path.join(exe_path, "Adobe Premiere Pro CC {}".format(last_version_info["DisplayName"].split(" ")[-1]))
    if not os.path.isdir(exe_path):
        raise IOError("Could not find install dir for Premiere in '{}'".format(exe_path))
    exe_path = os.path.join(exe_path, "Adobe Premiere Pro.exe")
    if not os.path.isfile(exe_path):
        raise IOError("Could not find Premiere executable in '{}'".format(exe_path))
    return exe_path


def start_premiere():
    """
    Start Premiere pro if not already started
    :return (int) pid of Premiere process
    """
    running, pid = exe_is_running("adobe premiere pro.exe")
    if running:
        return pid
    exe_path = get_last_premiere_exe()
    # we count the CEP pannel process running before because Premiere pops new ones at the end of loading
    start_running_cep_pannels = count_running_exe("CEPHtmlEngine.exe")
    # we don't call directly premiere exec here so it's not a child of this script.
    # It will still run after this script is killed
    call(["start_premiere.bat", exe_path])
    # check process is starting and when it is done
    for i in range(200):
        running, pid = exe_is_running("adobe premiere pro.exe")
        if not running:
            raise ValueError("Could not start premiere")
        current_running_cep_pannels = count_running_exe("CEPHtmlEngine.exe")
        if current_running_cep_pannels > start_running_cep_pannels:
            time.sleep(1)
            return pid
        time.sleep(0.5)
    raise SystemError("Could not guaranty premiere started")


if __name__ == "__main__":
    # print(get_installed_softwares_info("adobe premiere pro"))
    # print(exe_is_running("adobe premiere pro.exe"))
    print(start_premiere())

