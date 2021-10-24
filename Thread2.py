from os import write
import time

from PyQt5 import QtCore

class Thread2(QtCore.QThread):
    write_signal = QtCore.pyqtSignal(str)
    finished_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None, data=0):
        super(Thread2, self).__init__(parent)
        self.data=data

    def run(self):
        self.write_signal.emit('Thread2 running')
        self.write_signal.emit(self.data["t2_value1"])
        self.write_signal.emit(self.data["t2_value2"])
        self.write_signal.emit(self.data["t2_value3"])
        time.sleep(3)
        self.write_signal.emit('Do stuff here')
        time.sleep(3)
        self.finished_signal.emit()

    def stop(self):
        self.write_signal.emit('Stopping thread2')
        self.finished_signal.emit()
        self.terminate()
