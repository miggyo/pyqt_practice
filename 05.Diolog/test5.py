import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from_class = uic.loadUiType("test5.ui")[0]

class WindowClass(QMainWindow, from_class) : 
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Test5")

        self.btnName.clicked.connect(self.InputName)
        self.btnSeason.clicked.connect(self.InputSeason)
        self.btnColor.clicked.connect(self.InputColor)
        self.btnFont.clicked.connect(self.InputFont)
        self.btnFile.clicked.connect(self.OpenFile)
        self.lineEdit.returnPressed.connect(self.InputNumber)
        self.btnclear.clicked.connect(self.ClearText)


    def InputName(self) :
        text, ok = QInputDialog.getText(self,'QInputDialog - Name','User name : ')
        if ok and text :
            self.textEdit.append(text)


    
    def InputSeason(self) :
        items = ['Spring','Summer','Fall','Winter']

        item, ok = QInputDialog.getItem(self,'QInputDialog - season','season:',items,0,False)
        if ok and item :
            self.textEdit.append(item)
    def InputColor(self) :
        colors= QColorDialog.getColor()

        if colors.isValid :
            self.textEdit.append("Color")
    
            self.textEdit.selectAll()
            self.textEdit.setTextColor(colors)
            self.textEdit.moveCursor(QTextCursor.End)


    def InputFont(self) :
        Font,ok = QFontDialog.getFont()

        if ok and Font :
            info = QFontInfo(Font)
            self.textEdit.append(info.family() + info.styleName())
    
            self.textEdit.selectAll()
            self.textEdit.setFont(Font)
            self.textEdit.moveCursor(QTextCursor.End)

    def OpenFile(self) :
        name = QFileDialog.getOpenFileName(self,'Open File','./')


        if name[0]:
            with open(name[0], 'r') as file:
                data = file.read()
                self.textEdit.setText(data)

    def InputNumber(self) :
        text = self.lineEdit.text()

        if text.isdigit():
            self.textEdit.setText(text)

        else:
            QMessageBox.warning(self, 'QMessageBox - setText','Please enter only numbers.')
            self.lineEdit.clear()

    def ClearText(self) :
        self.textEdit.clear()


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())