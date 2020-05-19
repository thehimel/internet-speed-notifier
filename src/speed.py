import speedtest

# Custom Modules
from notify import notify
# from console import log


def bw_in_mb(bw_in_bytes):
    d = 1000000
    bw = bw_in_bytes/d

    # return bw with 2 decimal places
    # return f'{bw:.2f}'
    return round(bw, 2)


def test_speed(args):
    st = speedtest.Speedtest()
    result = {}
    """
    result = {
        downloadSpeed: 0,
        uploadSpeed: 0
    }
    """

    result['downloadSpeed'] = bw_in_mb(st.download())
    result['uploadSpeed'] = bw_in_mb(st.upload())
    # log(str(result))

    # result['downloadSpeed'] = 0.5
    # result['uploadSpeed'] = 0.5

    notify(result, args)
