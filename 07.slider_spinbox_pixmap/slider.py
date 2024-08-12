import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


from_class = uic.loadUiType("slider.ui")[0]



class WindowClass(QMainWindow, from_class) : 
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        min = self.spinBox.minimum()
        max = self.spinBox.maximum()
        step = self.spinBox.singleStep()

        self.editmin.setText(str(min))
        self.editmax.setText(str(max))
        self.editstep.setText(str(step))


        self.slider.setRange(min,max)
        self.slider.setSingleStep(step)
        
        self.btnApply.clicked.connect(self.apply)
        self.spinBox.valueChanged.connect(self.changeSpinBox)
        self.slider.valueChanged.connect(self.changeSlider)
        self.btnSave.clicked.connect(self.savePixmap) 
        self.btnOpen.clicked.connect(self.openPixmap)

        

        # self.pixMap.setPixmap(self.pixmap)
        # self.pixMap.resize(self.pixmap.width(),self.pixmap.height())
        
        
    def changeSlider(self):
        self.actualValue = self.slider.value()
        self.labelValue_2.setText(str(self.actualValue))
        self.spinBox.setValue(self.actualValue)


    def changeSpinBox(self):
        actualValue = self.spinBox.value()
        self.labelValue.setText(str(self.actualValue))
        self.slider.setValue(self.actualValue)
    
    def apply(self):
        min = self.editmin.text()
        max = self.editmax.text()
        step = self.editstep.text()
        
        self.spinBox.setRange(int(min), int(max))
        self.spinBox.setSingleStep(int(step))

        self.slider.setRange(int(min), int(max))
        self.slider.setSingleStep(int(step))


    def savePixmap(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Images (*.png *.jpg *.bmp)", options=options)

        if file_name:
            pixmap = self.pixmap
            pixmap.save(file_name)


                

    def openPixmap(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Images (*.png *.jpg *.bmp)')

        if name:
            pixmap = QPixmap(name)
            pixmap = pixmap.scaled(self.actualValue, self.actualValue)
            self.pixMap.setPixmap(pixmap)
            

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())
