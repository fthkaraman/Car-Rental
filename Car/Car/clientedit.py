# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'useredit.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3

import first



class Ui_Form(object):

    def add(self):
        tc = self.textEdit.toPlainText()
        name = self.textEdit_2.toPlainText()
        surname = self.textEdit_3.toPlainText()
        email = self.textEdit_4.toPlainText()
        phone = self.textEdit_5.toPlainText()
        address = self.textEdit_6.toPlainText()

        conn = sqlite3.connect('Our_data.db')
        conn.execute(''' INSERT INTO CLIENTS(TCNO,NAME,SURNAME,EMAIL,PHONE,ADDRESS) VALUES(?,?,?,?,?,?) ''',
                     (tc, name, surname, email, phone, address))
        conn.commit()

    def load(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        conn = sqlite3.connect('Our_data.db')
        content = 'SELECT * FROM CLIENTS'
        res = conn.execute(content)
        for row_index, row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        conn.close()
        return

    def delete(self):
        conn = sqlite3.connect('Our_data.db')
        curs = conn.cursor()
        content = 'SELECT * FROM CLIENTS'
        res = curs.execute(content)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                id = data[0]
                tc = data[1]
                name = data[2]
                surname = data[3]
                email = data[4]
                phone = data[5]
                address = data[6]
                curs.execute(''' DELETE FROM CLIENTS WHERE ID = ? AND TCNO = ? AND NAME = ? AND SURNAME = ? AND EMAIL = ? AND PHONE = ? AND ADDRESS = ? ''',(id,tc,name,surname,email,phone,address,))
                conn.commit()
                self.load()

    def update(self):
        conn = sqlite3.connect('Our_data.db')
        curs = conn.cursor()
        content = 'SELECT * FROM CLIENTS'
        res = curs.execute(content)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                tc = self.textEdit.getValueAt(data[0])
                name = self.textEdit_2.toPlainText(data[1])
                surname = self.textEdit_3.toPlainText(data[2])
                email = self.textEdit_4.toPlainText(data[3])
                phone = self.textEdit_5.toPlainText(data[4])
                address = self.textEdit_6.toPlainText(data[5])

                curs.execute(
                    ''' UPDATE CLIENTS SET TCNO = ? , NAME = ? , SURNAME = ? , EMAIL = ? , PHONE = ? , ADDRESS = ? WHERE ID = ?''',
                    (tc, name, surname, email, phone, address))
                conn.commit()
                self.load()



    def setupUi(self, Form):
        self.ekran = Form
        Form.setObjectName("Form")
        Form.resize(852, 470)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 100, 0, 255), stop:1 rgba(200, 50, 0, 255));\n"
"")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(120, 10, 181, 31))
        self.textEdit.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 60, 181, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(120, 110, 181, 31))
        self.textEdit_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(120, 170, 181, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 240, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.textEdit_5 = QtWidgets.QTextEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(120, 230, 181, 31))
        self.textEdit_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 290, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 410, 75, 23))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"border: 3px solid blue;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(320, 170, 501, 221))
        self.tableWidget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 20, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setObjectName("label_7")
        self.textEdit_6 = QtWidgets.QTextEdit(Form)
        self.textEdit_6.setGeometry(QtCore.QRect(120, 290, 181, 101))
        self.textEdit_6.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textEdit_6.setObjectName("textEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 410, 75, 23))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"border: 3px solid blue;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.delete)

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 410, 75, 23))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"border: 3px solid blue;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.load)

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 410, 75, 23))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                        "border: 3px solid blue;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.first)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Name"))
        self.label_3.setText(_translate("Form", "Surname"))
        self.label_4.setText(_translate("Form", "E-Mail"))
        self.label_5.setText(_translate("Form", "Phone"))
        self.label_6.setText(_translate("Form", "Address"))
        self.pushButton.setText(_translate("Form", "Add"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "TC No"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Surname"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "E-Mail"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Address"))
        self.label_7.setText(_translate("Form", "TC No"))
        self.pushButton_2.setText(_translate("Form", "Delete"))
        self.pushButton_4.setText(_translate("Form", "Load"))
        self.pushButton_5.setText(_translate("Form", "Back"))
    def first(self):
        self.screen = QtWidgets.QMainWindow()
        self.ui = first.Ui_MainWindow()
        self.ui.setupUi(self.screen)
        self.screen.show()
        self.ekran.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
