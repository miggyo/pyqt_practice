import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
import mysql.connector

from_class = uic.loadUiType("test7.ui")[0]



class WindowClass(QMainWindow, from_class) : 
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Test6")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.btnAdd.clicked.connect(self.Add)

    def Add(self):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidget(self.editName.text()))
        self.tableWidget.setItem(row, 1, QTableWidget(self.editGender.text()))
        self.tableWidget.setItem(row, 2, QTableWidget(self.editBirthday.text()))



if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())



