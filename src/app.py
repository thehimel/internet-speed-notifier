# #! C:\Python\Python37\python.exe

import time
from threading import Thread
import argparse

# Custom Modules
from speed import test_speed
from console import log
from check_connection import check_connection

parser = argparse.ArgumentParser(description='Network Speed Notifier')

parser.add_argument('-d', '--delay', type=float, metavar='', default=300, help='Delay in seconds for interval between tests')

parser.add_argument('-dl', '--dlower', type=float, metavar='', default=0.5, help='Lower bound of download speed to get special notification')
parser.add_argument('-du', '--dupper', type=float, metavar='', default=5.0, help='Upper bound of download speed to get special notification')

parser.add_argument('-ul', '--ulower', type=float, metavar='', default=0.5, help='Lower bound of upload speed to get special notification')
parser.add_argument('-uu', '--uupper', type=float, metavar='', default=3.0, help='Upper bound of upload speed to get special notification')

parser.add_argument('-ns', '--nospecial', action='store_true', help='Turn off the special notification')
parser.add_argument('-nv', '--novoice', action='store_true', help='Turn off the voice notification')
parser.add_argument('-nt', '--notoast', action='store_true', help='Turn off the Windows 10 toast notification')

args = parser.parse_args()


class WorkerThread(Thread):
    def __init__(self):
        super(WorkerThread, self).__init__()

    def run(self):
        # run the speed test
        test_speed(args)


class ProgressThread(Thread):
    def __init__(self, worker):
        super(ProgressThread, self).__init__()

        self.worker = worker

    def run(self):
        while True:
            if not self.worker.is_alive():
                # print('\n')
                log('\n')
                return True

            # print('.', end='')
            log('.')
            time.sleep(2.0)


def main():
    while True:
        if check_connection() is False:
            log('No internet connection!')
            break

        worker = WorkerThread()
        progress = ProgressThread(worker)
        worker.start()
        progress.start()
        progress.join()

        delay = args.delay
        time.sleep(delay)


if __name__ == '__main__':
    main()
