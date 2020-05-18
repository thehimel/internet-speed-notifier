#! C:\Python\Python37\python.exe

import time
from threading import Thread

# Custom Modules
from speed import test_speed
from console import log


class WorkerThread(Thread):
    def __init__(self):
        super(WorkerThread, self).__init__()

    def run(self):
        # run the speed test
        test_speed()


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


if __name__ == '__main__':
    while True:
        worker = WorkerThread()
        progress = ProgressThread(worker)
        worker.start()
        progress.start()
        progress.join()

        delay = 10.0
        time.sleep(delay)
