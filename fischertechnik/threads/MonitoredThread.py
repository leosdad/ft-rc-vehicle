import threading
import signal
import os


class MonitoredThread(threading.Thread):

    exception = None

    def run(self):
        monitor = threading.Thread(target=self._monitor, args=(), daemon=True)
        monitor.start()
        try:
            super().run()
        except Exception as e:
            self.exception = e

    def _monitor(self):
        self.join()
        if self.exception is not None:
            os.kill(os.getpid(), signal.SIGTERM)

