# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from first import Ui_MainWindow
import sqlite3


class Ui_Form(object):
    def setupUi(self, Form):
        self.screen = Form
        Form.setObjectName("Form")
        Form.resize(846, 470)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 851, 471))
        self.label.setStyleSheet("border-image: url(C:/Users/Fatih/Desktop/back.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(610, 40, 221, 31))
        self.textEdit.setStyleSheet("border: 2px solid blue;\n"
"\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(610, 110, 221, 31))
        self.textEdit_2.setStyleSheet("border: 2px solid blue;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(510, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(93, 144, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(510, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(93, 144, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(610, 170, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 100, 0, 255), stop:1 rgba(255, 100, 0, 255));\n")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.logincheck)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "User Name"))
        self.label_3.setText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Login"))

    def logincheck(self):
        username = self.textEdit.toPlainText()
        password = self.textEdit_2.toPlainText()

        connection = sqlite3.connect('Our_data.db')

        result = connection.execute(''' SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ? ''', (username,password))
        if(len(result.fetchall()) > 0):
            print('User found')
            self.mainwindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.mainwindow)
            self.mainwindow.show()
            self.screen.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
