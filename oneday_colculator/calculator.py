import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
import mysql.connector
import re


from_class = uic.loadUiType("calculator.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Test6")
        self.operator_flag = 0
        self.cal_on = 0  # 계산 여부 플래그
        self.first_input = True  # 초기에만 0이 아닌 숫자가 입력되도록 하는 플래그
        self.point_flag = False
        self.first_zero = False
        self.current_text = []

        self.btnOne.clicked.connect(self.write)
        self.btnTwo.clicked.connect(self.write)
        self.btnThree.clicked.connect(self.write)
        self.btnFour.clicked.connect(self.write)
        self.btnFive.clicked.connect(self.write)
        self.btnSix.clicked.connect(self.write)
        self.btnSeven.clicked.connect(self.write)
        self.btnEight.clicked.connect(self.write)
        self.btnNine.clicked.connect(self.write)
        self.btnZero.clicked.connect(self.write)
        self.btnPlus.clicked.connect(self.write)
        self.btnMinus.clicked.connect(self.write)
        self.btnMultiple.clicked.connect(self.write)
        self.btnPoint.clicked.connect(self.write)
        self.btnSl.clicked.connect(self.write)
        self.btnEqual.clicked.connect(self.calculate)
        self.btnAC.clicked.connect(self.ac_reset)
            
       

    def write(self):
        button = self.sender() 
        self.cal_input.setTextColor(QColor("black"))
        self.cal_input.setFont(QFont("Arial", 12, QFont.Normal))
        
        if button is not None:            
            self.text = button.text()
            self.current_text = self.cal_input.toPlainText()
            if self.cal_on==1:
                self.ac_reset()
                self.input_rule()
                
            else:
                self.input_rule()

    def input_rule(self):
        if self.first_input == True:  # 초기에만 0이 아닌 숫자가 입력될 때
            if self.cal_on==1:
                self.cal_input.clear()
                self.cal_on=0
                self.cal_input.insertPlainText(self.text)

            elif self.text in ['*', '/']:  # *,/도 못오져~
                pass

            elif self.text != '0' and re.match(r'\d', self.text):  
                self.cal_input.insertPlainText(self.text)
                self.operator_flag = 0
                self.point_flag = 1
                self.first_input = False

            elif self.operator_flag == False and self.text in ['+', '-']:  # 연산자 중복입력 방지 연산자가 한번 눌리면 첫입력으로 변경
                self.cal_input.insertPlainText(self.text)
                self.operator_flag = True

            elif self.text == '0': #처음이 0이면!!!
                self.cal_input.insertPlainText(self.text)
                self.point_flag = 1
                self.first_input = False
                self.operator_flag =False
                self.first_zero =True

            elif self.text == '.': #처음이 .이면!!!!
                self.cal_input.insertPlainText('0' + self.text)
                self.point_flag = 1
                self.first_input = False

        elif self.first_input == False:  # 처음 숫자가 눌린후
            if self.operator_flag == False and self.text in ['+', '-', '*', '/']:  # 연산자 중복입력 방지 연산자가 한번 눌리면 첫입력으로 변경
                self.cal_input.insertPlainText(self.text)
                self.operator_flag = True
                self.first_input = True
            elif re.match(r'\d', self.text):  # 숫자 입력
                if self.first_zero == False:
                    self.cal_input.insertPlainText(self.text)
                    self.operator_flag =False
            elif self.text == '.': #마지막버튼이 숫자면!!!
                if  self.point_flag ==1 and self.current_text[-1] != '.':
                    self.cal_input.insertPlainText(self.text)
                    self.point_flag = 0
                    self.first_zero = False
            

    def ac_reset(self):

        self.cal_input.clear()
        result = 0
        self.cal_on=0
        self.operator_flag = 0
        self.first_input = True  # 초기에만 0이 아닌 숫자가 입력되도록 하는 플래그
        self.point_flag = False
        self.current_text = []

    def calculate(self):
            expression = self.cal_input.toPlainText()
            self.cal_on=1
            try:
                result = eval(expression)
                self.cal_input.clear()
                self.cal_input.setFont(QFont("Arial", 12, QFont.Bold))
                self.cal_input.setTextColor(QColor("blue")) 
                self.cal_input.setText(str(result))

            except Exception as e:
                self.cal_input.setText("Error")
    


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())
