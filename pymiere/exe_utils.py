import os
from subprocess import check_output
try:
    import _winreg as wr  # python 2
except:
    import winreg as wr  # python 3

def exe_is_running(exe_name):
    """
    Using tasklist windows command, we can find if a specific process is running
    :param exe_name: (str) exact name of the process (ex : 'pycharm64.exe')
    :return: (bool) exe is running
    """
    # use tasklist command with filter by name
    call = 'TASKLIST', '/FI', 'imagename eq {}'.format(exe_name)
    output = check_output(call, text=True)
    # check in last line for process name
    last_line = output.strip().splitlines()[-1]
    return last_line.lower().startswith(exe_name.lower())

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
    premiere_versions = get_installed_softwares_info("adobe premiere pro")
    if not premiere_versions:
        raise OSError("Could not find an Adobe Premiere Pro version installed on this computer")


if __name__ == "__main__":
    print(get_installed_softwares_info("adobe premiere pro"))
    print(exe_is_running("adobe premiere pro.exe"))