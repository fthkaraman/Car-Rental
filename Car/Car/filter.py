# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3

import first


class Ui_Form(object):
    def setupUi(self, Form):
        self.ekran = Form
        Form.setObjectName("Form")
        Form.resize(818, 447)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 113, 426))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_4.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_4.addWidget(self.checkBox_2)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout.addWidget(self.checkBox_9)
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout.addWidget(self.checkBox_11)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_3.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_3.addWidget(self.checkBox_6)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_7.setStyleSheet("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_2.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_2.addWidget(self.checkBox_8)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.clicked.connect(self.load)
        self.pushButton.setGeometry(QtCore.QRect(320, 310, 321, 41))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border: 1px solid blue;\n"
"border-radius: 20px;\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.clicked.connect(self.first)
        self.pushButton_2.clicked.connect(self.load)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 360, 100, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 0);\n"
                                      "border: 1px solid blue;\n"
                                      "border-radius: 20px;\n"
                                      "")
        self.pushButton.setObjectName("pushButton_2")

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(190, 10, 581, 291))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Brand"))
        self.checkBox.setText(_translate("Form", "Opel"))
        self.checkBox_3.setText(_translate("Form", "Volkswagen"))
        self.checkBox_2.setText(_translate("Form", "Renault"))
        self.groupBox_4.setTitle(_translate("Form", "Vehicle Type"))
        self.checkBox_9.setText(_translate("Form", "Sedan"))
        self.checkBox_11.setText(_translate("Form", "Hatchback"))
        self.groupBox_2.setTitle(_translate("Form", "Fuel Type"))
        self.checkBox_5.setText(_translate("Form", "Gasoline"))
        self.checkBox_6.setText(_translate("Form", "Diesel"))
        self.groupBox_3.setTitle(_translate("Form", "Gear Type"))
        self.checkBox_7.setText(_translate("Form", "Automatic"))
        self.checkBox_8.setText(_translate("Form", "Manual"))
        self.pushButton.setText(_translate("Form", "Choose "))
        self.pushButton_2.setText(_translate("Form", "Back "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Brand"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Model"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Vehicle Type"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Fuel Type"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Gear Type"))

    def load(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        conn = sqlite3.connect('Our_data.db')

        if self.checkBox.isChecked():
            content = 'SELECT * FROM CARS WHERE BRAND = "Opel"'
            res = conn.execute(content)
            for row_index, row_data in enumerate(res):
                self.tableWidget.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        if self.checkBox_3.isChecked():
            content = 'SELECT * FROM CARS WHERE BRAND = "Volkswagen"'
            res = conn.execute(content)
            for row_index, row_data in enumerate(res):
                self.tableWidget.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        if self.checkBox_2.isChecked():
            content = 'SELECT * FROM CARS WHERE BRAND = "Renault"'
            res = conn.execute(content)
            for row_index, row_data in enumerate(res):
                self.tableWidget.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        if  self.checkBox_9.isChecked():
            content = 'SELECT * FROM CARS WHERE VEHICLE = "Sedan"'
            res = conn.execute(content)
            for row_index, row_data in enumerate(res):
                self.tableWidget.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        if  self.checkBox_11.isChecked():
            content = 'SELECT * FROM CARS WHERE VEHICLE = "Hatchback"'
            res = conn.execute(content)
            for row_index, row_data in enumerate(res):
                self.tableWidget.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        if  self.checkBox_5.isChecked():
            content = 'SELECT * FROM CARS WHERE FUEL = "Gasoline"'
            res = conn.execute(content)
            for row_index, row_data in enumerate(res):
                self.tableWidget.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        if  self.checkBox_6.isChecked():
            content = 'SELECT * FROM CARS WHERE FUEL = "Diesel"'
            res = conn.execute(content)
            for row_index, row_data in enumerate(res):
                self.tableWidget.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        if  self.checkBox_7.isChecked():
            content = 'SELECT * FROM CARS WHERE GEAR = "Automatic"'
            res = conn.execute(content)
            for row_index, row_data in enumerate(res):
                self.tableWidget.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        if  self.checkBox_8.isChecked():
            content = 'SELECT * FROM CARS WHERE GEAR = "Manuel"'
            res = conn.execute(content)
            for row_index, row_data in enumerate(res):
                self.tableWidget.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        conn.close()
        return

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
