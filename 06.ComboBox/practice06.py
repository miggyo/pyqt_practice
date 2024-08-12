import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
import mysql.connector
from_class = uic.loadUiType("practice06.ui")[0]
remote = mysql.connector.connect(
    host = "database-1.cdsoiiswk6c2.ap-northeast-2.rds.amazonaws.com",
    port = 3306,
    user = "robot",
    password = "6074",
    database = "amrbase"
)
cursor = remote.cursor(buffered=True)
cursor.execute("select * from celeb")
result = cursor.fetchall()
#콤보박스 목록!!설정하기
#birthday
cursor.execute("SELECT MIN(birthday), MAX(birthday) FROM celeb")
min_max_birthday = cursor.fetchone()
min_birthday = min_max_birthday[0]
max_birthday = min_max_birthday[1]
#gender
cursor.execute("select distinct sex from celeb")
gender = cursor.fetchall()
gender_items = ["All"]
for row in gender:
    gender_items.append(row[0])
#agency
cursor.execute("select distinct agency from celeb")
agency = cursor.fetchall()
agency_items = ["All"]
for row in agency:
    agency_items.append(row[0])
#jobtitle
cursor.execute("select distinct job_title from celeb")
job_title = cursor.fetchall()
job_items = [job.strip() for row in job_title for job in row[0].split(',')]
job_items = list(set(job_items))
job_items = sorted(job_items)
job_items.insert(0, "All")
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("practice06")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.btnSearch.clicked.connect(self.Search)
        self.btnReset.clicked.connect(self.Reset)
        self.dateEdit_st.setDate(min_birthday)
        self.dateEdit_end.setDate(max_birthday)
        self.cbSex.addItems(gender_items)
        self.cbAgency.addItems(agency_items)
        self.cbJobTitle.addItems(job_items)
    def Search(self):
        start_date = self.dateEdit_st.date().toPyDate()
        end_date = self.dateEdit_end.date().toPyDate()
        gender = self.cbSex.currentText()
        agency = self.cbAgency.currentText()
        job = self.cbJobTitle.currentText()
        filtered_result = [row for row in result if start_date <= row[2] <= end_date]
        if (gender != "All" or agency != "All" or job != "All"):
            filtered_result = [row for row in filtered_result if start_date <= row[2] <= end_date and
                            (gender == "All" or row[4] == gender) and
                            (agency == "All" or row[5] == agency) and
                            (job == "All" or any(job == j.strip() for j in row[6].split(',')))]
        if filtered_result:
            self.tableWidget.setRowCount(len(filtered_result))
            self.tableWidget.setColumnCount(len(filtered_result[0]))
            for row, rowData in enumerate(filtered_result):
                for col, value in enumerate(rowData):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, col, item)
        else:
            QMessageBox.warning(self, "검색 결과", "검색 결과가 없습니다.", QMessageBox.Ok)
        column_widths = {}
    def Reset(self):
        self.dateEdit_st.setDate(min_birthday)
        self.dateEdit_end.setDate(max_birthday)
        self.cbSex.setCurrentIndex(0)
        self.cbAgency.setCurrentIndex(0)
        self.cbJobTitle.setCurrentIndex(0)
        self.Search()
if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())