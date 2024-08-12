import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *

import serial
import struct

class Receiver(QThread):
    detected = pyqtSignal(bytes)
    recvTotal = pyqtSignal(int)
    def __init__(self, conn, parent = None):
        super(Receiver, self).__init__(parent)
        self.is_running = False
        self.conn = conn
        print("recv init")
    def run(self):
        print("recv start")
        self.is_running = True
        while (self.is_running == True):
            if self.conn.readable():
                res = self.conn.read_until(b'\n')
                if len(res) > 0:
                    res = res[:-2]
                    cmd = res[:2].decode()
                    if cmd == 'GS' and res[2] == 0:
                        print("recv detected")
                        self.detected.emit(res[3:])
                    elif cmd == 'GT' and res[2] == 0:
                        print("recvTotal")
                        print(len(res))
                        self.recvTotal.emit(int.from_bytes(res[3:7], 'little'))
                    else:
                        print("unknown error")
                        print(res)
    def stop(self):
        print("recv stop")
        self.is_running = False


from_class = uic.loadUiType("withArduino.ui")[0]


class WindowClass(QMainWindow, from_class): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.uid = bytes(4)
        self.conn = serial.Serial(port = '/dev/ttyACM1', baudrate = 9600, timeout = 1)
        self.recv = Receiver(self.conn)
        self.recv.start()

        self.recv.detected.connect(self.detected)

        self.btnReset.clicked.connect(self.reset)
        self.btnCharge.clicked.connect(self.charge)
        self.btnPay.clicked.connect(self.pay)

        self.disable()

        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.getStatus)
        self.timer.start()


    def reset(self):
        print("reset")
        return


    def charge(self):
        print("charge")
        return
    

    def pay(self):
        print("pay")
        return
    

    def enable(self, total):
        self.totalLabel.setText(str(total))
        self.ChargeEdit.setDisabled(False)
        self.btnCharge.setDisabled(False)
        self.PayEdit.setDisabled(False)
        self.btnPay.setDisabled(False)


    def disable(self):
        self.moneyStatus.setText(str('-'))
        self.ChargeEdit.setDisabled(True)
        self.btnCharge.setDisabled(True)
        self.PayEdit.setDisabled(True)
        self.btnPay.setDisabled(True)

    def detected(self, uid):
        print('detected')
        self.uid = uid
        self.timer.stop()
        self.enable(0)
        return

    def send(self, command, data = 0):
        print('send')
        req_data = struct.pack('<2s4sic', command, self.uid, data, b'\n')
        self.conn.write(req_data)
        return
    

    def getStatus(self):
        print('getStatus')
        self.send(b'GS')
        return
    
    def getTotal(self):
        print('getTotal')
        self.send(b'GT')
        return

    def setTotal(self,total):
        print('setTotal')
        self.send(b'ST',total)
        return
  
if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())
