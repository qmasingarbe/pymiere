"""
Suite of function used to manipulate Premiere Pro app (is it running ? start it...)
Tested on Windows 10 and macOS Catalinq
Should work fine but no guaranty is provided...
"""
import os
import sys
import time
import re
import json
import subprocess
from distutils.version import StrictVersion
import platform
if platform.system().lower() == "windows":
    WINDOWS_SYSTEM = True
    try:
        import _winreg as wr  # python 2
    except:
        import winreg as wr  # python 3
else:
    # if not windows, assume it is a macOS
    WINDOWS_SYSTEM = False


CREATE_NO_WINDOW = 0x08000000
PREMIERE_PROCESS_NAME = "adobe premiere pro.exe" if WINDOWS_SYSTEM else "Adobe Premiere Pro"
CEPPANEL_PROCESS_NAME = "CEPHtmlEngine.exe" if WINDOWS_SYSTEM else "CEPHtmlEngine"


def is_premiere_running():
    """
    Is there a running instance of the Premiere Pro app on this machine ?

    :return: (bool) process is running, (int) pid
    """
    return exe_is_running(PREMIERE_PROCESS_NAME)


def start_premiere(use_bat=False):
    """
    Start Premiere pro if not already started

    :param use_bat: (bool) start Premiere Pro using a bat file to keep it running after script exit (in specific cases, windows only)
    :return (int) pid of Premiere process
    """
    running, pid = is_premiere_running()
    if running:
        return pid

    exe_path = get_last_premiere_exe()
    # we count the CEP pannel process running before because Premiere pops new ones at the end of loading
    start_running_cep_pannels = count_running_exe(CEPPANEL_PROCESS_NAME)

    if use_bat and WINDOWS_SYSTEM:
        # we don't call directly premiere exec here so it's not a child of this script.
        # It will still run after this script is killed (seems to be always the case except in Pycharm...)
        subprocess.call([os.path.join(__file__, "..", "bin", "start_premiere.bat"), exe_path])
    elif WINDOWS_SYSTEM:
        subprocess.Popen(exe_path, creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.Popen(["open", exe_path])

    # check process is starting and when it is done
    for i in range(200):
        time.sleep(0.5)
        running, pid = exe_is_running(PREMIERE_PROCESS_NAME)
        if not running:
            raise ValueError("Could not start premiere")
        current_running_cep_pannels = count_running_exe(CEPPANEL_PROCESS_NAME)
        if current_running_cep_pannels > start_running_cep_pannels:
            time.sleep(1)
            return pid
    raise SystemError("Could not guaranty premiere started")


def exe_is_running(exe_name):
    """
    List processes by name to know if one is running

    :param exe_name: (str) exact name of the process (ex : 'pycharm64.exe' for windows or 'Safari' for mac)
    :return: (bool) process is running, (int) pid
    """
    pids = _get_pids_from_name(exe_name)
    if len(pids) == 0:
        return False, None
    if len(pids) > 1:
        raise OSError("More than one process matching name '{}' were found running (pid: {})".format(exe_name, pids))
    return True, pids[0]


def count_running_exe(exe_name):
    """
    List processes by name to know how many are running

    :param exe_name: (str) exact name of the process (ex : 'pycharm64.exe' for windows or 'Safari' for mac)
    :return: (int) Number of process with given name running
    """
    return len(_get_pids_from_name(exe_name))


def get_last_premiere_exe():
    """
    Get the executable path on disk of the last installed Premiere Pro version

    :return: (str) path to executable
    """
    get_last_premiere_exe_func = _get_last_premiere_exe_windows if WINDOWS_SYSTEM else _get_last_premiere_exe_mac
    return get_last_premiere_exe_func()


def _get_pids_from_name(process_name):
    """
    Given a process name get ids of running process matching this name

    :param process_name: (str) process name (ex : 'pycharm64.exe' for windows or 'Safari' for mac)
    :return: (list of int) pids
    """
    if WINDOWS_SYSTEM:
        # use tasklist windows command with filter by name
        call = 'TASKLIST', '/FI', 'imagename eq {}'.format(process_name)
        output = subprocess.check_output(call, creationflags=CREATE_NO_WINDOW)
        if sys.version_info >= (3, 0):
            output = output.decode(encoding="437")  # encoding for windows console
        # parse output lines
        lines = output.strip().splitlines()
        matching_lines = [l for l in lines if l.lower().startswith(process_name.lower())]
        return [int(re.findall(l[:len(process_name)] + "\ +([0-9]{1,6}) ", l)[0]) for l in matching_lines]
    else:
        # use pgrep UNIX command to filter processes by name
        try:
            output = subprocess.check_output(["pgrep", process_name])
        except subprocess.CalledProcessError:  # pgrep seems to crash if the given name is not a running process...
            return list()
        # parse output lines
        lines = output.strip().splitlines()
        return list(map(int, lines))


# ----- platform specific functions -----
def _get_last_premiere_exe_windows():
    """
    WINDOWS ONLY
    Get the executable path on disk of the last installed Premiere Pro version using windows registry

    :return: (str) path to executable
    """
    premiere_versions = _get_installed_softwares_info("adobe premiere pro")
    if not premiere_versions:
        raise OSError("Could not find an Adobe Premiere Pro version installed on this computer")
    # find last installed version
    last_version_num = sorted([StrictVersion(v["DisplayVersion"]) for v in premiere_versions])[-1]
    last_version_info = [v for v in premiere_versions if v["DisplayVersion"] == str(last_version_num)][0]
    # search actual exe path
    base_path = last_version_info["InstallLocation"]
    build_year = last_version_info["DisplayName"].split(" ")[-1]
    wrong_paths = list()
    for folder_name in ["Adobe Premiere Pro CC {}", "Adobe Premiere Pro {}", ""]:  # different versions formatting
        exe_path = os.path.join(base_path, folder_name.format(build_year), "Adobe Premiere Pro.exe")
        if not os.path.isfile(exe_path):
            wrong_paths.append(exe_path)
            continue
        wrong_paths = list()
        break
    if len(wrong_paths) != 0:
        raise IOError("Could not find Premiere executable in '{}'".format(wrong_paths))
    return exe_path


def _get_last_premiere_exe_mac():
    """
    MACOS ONLY
    Get the executable path on disk of the last installed Premiere Pro version using macOS System Profiler

    :return: (str) path to executable
    """
    # list all installed app to a json datastructure
    output = subprocess.check_output(["system_profiler", "-json", "SPApplicationsDataType"])
    apps_data = json.loads(output)["SPApplicationsDataType"]
    # filter Premiere pro installed versions
    premiere_apps = [data for data in apps_data if "adobe premiere pro" in data["_name"].lower()]
    if not premiere_apps:
        raise OSError("Could not find an Adobe Premiere Pro version installed on this computer")
    # get last app version path
    premiere_apps.sort(key=lambda d: d["version"], reverse=True)
    return premiere_apps[0]["path"]


def _get_installed_softwares_info(name_filter, names=["DisplayVersion", "InstallLocation"]):
    """
    WINDOWS ONLY
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


if __name__ == "__main__":
    # print(get_installed_softwares_info("adobe premiere pro"))
    # print(exe_is_running("adobe premiere pro.exe"))
    print(start_premiere())
