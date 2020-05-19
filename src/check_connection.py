# https://www.codespeedy.com/how-to-check-the-internet-connection-in-python/

import urllib.request


def check_connection(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except Exception:
        return False
