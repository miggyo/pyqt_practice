import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from_class = uic.loadUiType("test6.ui")[0]

class WindowClass(QMainWindow, from_class) : 
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Test6")

        for year in range(1900,2023 + 1):
            self.cbYear.addItem(str(year))

        
        for month in range(1,12 + 1):
            self.cbMonth.addItem(str(month))

        for day in range(1,31 + 1):
            self.cbDay.addItem(str(day))

        self.cbYear.setCurrentText(str(1990))
        self.cbDay.currentIndexChanged.connect(self.printBirthday) #날짜바꾸면 바뀜
        self.calendarWidget.clicked.connect(self.selectDate)

    def printBirthday(self):
        year = self.cbYear.currentText()
        month = self.cbMonth.currentText()
        day = self.cbDay.currentText()
        self.lineEdit.setText(year+month.zfill(2)+day.zfill(2))

    def selectDate(self):
        date = self.calendarWidget.selectedDate()
        year = date.toString('yyyy')
        month = date.toString('M')
        day = date.toString('d')

        self.cbYear.setCurrentText(year)
        self.cbMonth.setCurrentText(month)
        self.cbDay.setCurrentText(day)
        self.lineEdit.setText(year+month.zfill(2)+day.zfill(2))
        
        


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())
