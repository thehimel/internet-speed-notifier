import subprocess

from console import log


def connect(ssid):
    cmd = f'netsh wlan connect name="{ssid}" ssid="{ssid}"'
    k = subprocess.run(cmd, capture_output=True, text=True).stdout
    log(k)


# connect('Your Network Name')
