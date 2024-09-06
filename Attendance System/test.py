from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import test2
import dataset
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Password",
    database = "Attendance"
)
cur = db.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 853)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Home = QtWidgets.QPushButton(self.centralwidget)
        self.Home.setGeometry(QtCore.QRect(40, 80, 111, 31))
        self.Home.setObjectName("Home")
        self.mark_attendance = QtWidgets.QPushButton(self.centralwidget)
        self.mark_attendance.setGeometry(QtCore.QRect(40, 190, 111, 31))
        self.mark_attendance.setObjectName("mark_attendance")
        self.Register = QtWidgets.QPushButton(self.centralwidget)
        self.Register.setGeometry(QtCore.QRect(40, 300, 111, 31))
        self.Register.setObjectName("Register")
        self.view_attendance = QtWidgets.QPushButton(self.centralwidget)
        self.view_attendance.setGeometry(QtCore.QRect(40, 390, 121, 31))
        self.view_attendance.setObjectName("view_attendance")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(250, 30, 881, 811))
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.label = QtWidgets.QLabel(self.page1)
        self.label.setGeometry(QtCore.QRect(120, 50, 611, 61))
        self.label.setStyleSheet("font: 75 14pt \"Microsoft JhengHei\";\n"
"color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 75 20pt \"Yu Gothic UI\";")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.page1)
        self.label_5.setGeometry(QtCore.QRect(190, 220, 501, 501))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../Downloads/face_recognition.gif"))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.page1)
        self.label_7.setGeometry(QtCore.QRect(0, 10, 871, 771))
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.stackedWidget.addWidget(self.page1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.text_roll = QtWidgets.QTextEdit(self.page_2)
        self.text_roll.setGeometry(QtCore.QRect(310, 270, 251, 41))
        self.text_roll.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_roll.setObjectName("text_roll")
        self.text_sub = QtWidgets.QTextEdit(self.page_2)
        self.text_sub.setGeometry(QtCore.QRect(310, 330, 251, 41))
        self.text_sub.setStyleSheet("color: rgb(255, 255, 255);")
        self.text_sub.setObjectName("text_sub")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(130, 270, 171, 41))
        self.label_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_13 = QtWidgets.QLabel(self.page_2)
        self.label_13.setGeometry(QtCore.QRect(130, 330, 171, 41))
        self.label_13.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_13.setObjectName("label_13")
        self.label_2.setObjectName("label_2")
        self.page_2_submit = QtWidgets.QPushButton(self.page_2)
        self.page_2_submit.setGeometry(QtCore.QRect(250, 370, 181, 41))
        self.page_2_submit.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.page_2_submit.setObjectName("page_2_submit")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 641, 131))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../../Downloads/loading_1.gif"))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(4, 5, 861, 771))
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.text_roll.raise_()
        self.label_2.raise_()
        self.page_2_submit.raise_()
        self.label_6.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(120, 310, 161, 21))
        self.label_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(120, 370, 161, 21))
        self.label_4.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.textEdit_name = QtWidgets.QTextEdit(self.page_3)
        self.textEdit_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit_name.setGeometry(QtCore.QRect(280, 310, 201, 31))
        self.textEdit_name.setObjectName("textEdit_name")
        self.textEdit_roll = QtWidgets.QTextEdit(self.page_3)
        self.textEdit_roll.setGeometry(QtCore.QRect(280, 370, 201, 31))
        self.textEdit_roll.setObjectName("textEdit_roll")
        self.textEdit_roll.setStyleSheet("color: rgb(255, 255, 255);")
        self.register_user = QtWidgets.QPushButton(self.page_3)
        self.register_user.setGeometry(QtCore.QRect(230, 460, 93, 28))
        self.register_user.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.register_user.setObjectName("register_user")
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 851, 751))
        self.label_9.setObjectName("label_9")
        self.label_9.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_13.raise_()
        self.text_sub.raise_()
        self.textEdit_name.raise_()
        self.textEdit_roll.raise_()
        self.register_user.raise_()     
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.tableWidget = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget.setGeometry(QtCore.QRect(530, 70, 281, 421))
        self.tableWidget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.load = QtWidgets.QPushButton(self.page_4)
        self.load.setGeometry(QtCore.QRect(80, 270, 251, 31))
        self.load.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.load.setObjectName("load")
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 861, 751))
        self.label_10.setObjectName("label_10")
        self.textEdit_sub = QtWidgets.QTextEdit(self.page_4)
        self.textEdit_sub.setGeometry(QtCore.QRect(150, 100, 231, 41))
        self.textEdit_sub.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.textEdit_sub.setObjectName("textEdit_sub")
        self.textEdit_5 = QtWidgets.QTextEdit(self.page_4)
        self.textEdit_5.setGeometry(QtCore.QRect(150, 180, 231, 41))
        self.textEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setGeometry(QtCore.QRect(20, 110, 121, 21))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setGeometry(QtCore.QRect(20, 190, 121, 21))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.label_10.raise_()
        self.tableWidget.raise_()
        self.load.raise_()
        self.textEdit_sub.raise_()
        self.textEdit_5.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        def load1(sub,date):
                self.tableWidget.setRowCount(0)
                value = f"{sub}{date}"
                cur.execute(f"select * from {sub}{date}")
                result = cur.fetchall()
                for row_num, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_num)
                        for column_num, data in enumerate(row_data):
                                self.tableWidget.setItem(row_num,column_num,QtWidgets.QTableWidgetItem(str(data)) )
                db.commit()
                


        self.Home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page1))
        self.mark_attendance.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.Register.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.view_attendance.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        
        self.page_2_submit.clicked.connect(lambda: test2.main1(self.text_roll.toPlainText(),self.text_sub.toPlainText()))
        self.register_user.clicked.connect(lambda: dataset.main1(self.textEdit_name.toPlainText(),self.textEdit_roll.toPlainText()))
        self.load.clicked.connect(lambda: load1(self.textEdit_sub.toPlainText(),self.textEdit_5.toPlainText()))

        self.face = QtGui.QMovie("..//..//..//Downloads//face_recognition.gif")
        self.label_5.setMovie(self.face)
        self.face.start()

        self.loading = QtGui.QMovie("..//..//..//Downloads//initial.gif")
        self.label_6.setMovie(self.loading)
        self.loading.start()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Home.setText(_translate("MainWindow", "Home"))
        self.mark_attendance.setText(_translate("MainWindow", "Mark Attendance"))
        self.Register.setText(_translate("MainWindow", "Register"))
        self.view_attendance.setText(_translate("MainWindow", "View Attendance"))
        self.label.setText(_translate("MainWindow", "Welcome to Student Attendance System"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "Enter Roll no : "))
        self.page_2_submit.setText(_translate("MainWindow", "Submit"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Enter Name: "))
        self.label_4.setText(_translate("MainWindow", "Enter Roll no: "))
        self.label_13.setText(_translate("MainWindow", "Enter Sub : "))
        self.register_user.setText(_translate("MainWindow", "Register"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.load.setText(_translate("MainWindow", "load"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "Enter Subject: "))
        self.label_12.setText(_translate("MainWindow", "Enter Date: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    cur.close()
