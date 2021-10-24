from os import write
import time

from PyQt5 import QtCore

class Thread1(QtCore.QThread):
    write_signal = QtCore.pyqtSignal(str)
    finished_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None, data=0):
        super(Thread1, self).__init__(parent)
        self.data=data

    def run(self):
        self.write_signal.emit('Thread1 running')
        self.write_signal.emit(self.data["t1_value1"])
        self.write_signal.emit(self.data["t1_value2"])
        time.sleep(3)
        self.write_signal.emit('Do stuff here')
        time.sleep(3)
        self.finished_signal.emit()

    def stop(self):
        self.write_signal.emit('Stopping thread1')
        self.finished_signal.emit()
        self.terminate()
