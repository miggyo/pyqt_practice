import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


from_class = uic.loadUiType("painter.ui")[0]

class WindowClass(QMainWindow, from_class) : 
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("painter")
        self.pixmap = QPixmap(self.label.width(),self.label.height())
        self.pixmap.fill(Qt.white)

        self.label.setPixmap(self.pixmap)
        self.draw()


    def draw(self):
        painter = QPainter(self.label.pixmap())
        painter.drawLine(100,100,500,100)

        self.line = QLine(100,200,500,200)
        painter.drawLine(self.line)
        self.p1 = QPoint(100,300)
        self.p2 = QPoint(500,300)
        painter.drawLine(self.p1,self.p2)
        painter.end


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())