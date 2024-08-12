import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from_class = uic.loadUiType("text.ui")[0]

class WindowClass(QMainWindow, from_class) : 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Text,QT!")

        self.pushButton_1.clicked.connect(self.button1_Clicked)
        self.pushButton_2.clicked.connect(self.button2_Clicked)
        self.pushButton_3.clicked.connect(self.button3_Clicked)

        self.radio_1.clicked.connect(self.Radio_Clicked)
        self.radio_2.clicked.connect(self.Radio_Clicked)
        self.radio_3.clicked.connect(self.Radio_Clicked)

    def button1_Clicked(self) :
        self.textEdit.setText("Button 1")
        self.radio_1.setChecked(True)
    def button2_Clicked(self) :
        self.textEdit.setText("Button 2") 
        self.radio_2.setChecked(True)
    def button3_Clicked(self) :
        self.textEdit.setText("Button 3")
        self.radio_3.setChecked(True)



    def Radio_Clicked(self):
        if self.radio_1.isChecked():
            self.textEdit.setText("Radio 1")
        elif self.radio_2.isChecked():
            self.textEdit.setText("Radio 2")
        elif self.radio_3.isChecked():
            self.textEdit.setText("Radio 3")
        else :
            self.textEdit.setText("Unkown")


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())