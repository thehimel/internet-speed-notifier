#! C:\Python\Python37\python.exe

import speedtest
import time

# Custom Modules
from notify import notify

st = speedtest.Speedtest()


def bw_in_mb(bw_in_bytes):
    d = 1000000
    bw = bw_in_bytes/d

    # return bw with 2 decimal places
    # return f'{bw:.2f}'
    return round(bw, 2)


while True:
    download_speed = bw_in_mb(st.download())
    upload_speed = bw_in_mb(st.upload())
    # download_speed = 2
    # upload_speed = 2

    notify(download_speed, upload_speed)
    delay = 300
    time.sleep(delay)
