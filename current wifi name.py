import subprocess

if __name__ == '__main__':
    import subprocess

    netInfo = str(subprocess.check_output(["netsh", "wlan", "show", "network"]))
    netInfo = netInfo.replace('\\r', '').replace("b' ", '').replace(":", '\n').replace("\\n", '\n')
    netInfo = netInfo.splitlines()
    connectedWifiName = netInfo[6][1:]
    print(connectedWifiName)
