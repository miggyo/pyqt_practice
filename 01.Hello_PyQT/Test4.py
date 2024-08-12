import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("Test4.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__ ()
        self.setupUi(self)
        self.setWindowTitle("Test3")

        self.pushButton.clicked.connect(self.addText)
        self.FontNanumGothic.clicked.connect(lambda : self.setFont("NanumGothic"))
        self.FontUbuntu.clicked.connect(lambda : self.setFont("Ubuntu"))

        self.RED.clicked.connect(lambda : self.setTextColor(255,0,0))
        self.GREEN.clicked.connect(lambda : self.setTextColor(0,255,0))
        self.BLUE.clicked.connect(lambda : self.setTextColor(0,0,255))

        self.SetFontSize.clicked.connect(self.setTextSize)

    def addText(self):
        input = self.Input.toPlainText()
        self.Input.clear()
        self.Output.append(input)

        
    def setFont(self,fontName):
        font=QFont(fontName,11)
        self.Output.setFont(font)

    def setTextColor(self,r,g,b):
        color = QColor(r,g,b)
        self.Output.selectAll()
        self.Output.setTextColor(color)
        self.Output.moveCursor(QTextCursor.End)

    def setTextSize(self):
        #size = int(self.FontSize.text())
        int_validator = QIntValidator()
        size = self.FontSize.setValidator(int_validator)#line edit
        self.Output.selectAll()
        self.Output.setTextSize(size)
        self.Output.moveCursor(QTextCursor.End)


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())