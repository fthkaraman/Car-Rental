# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rent.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

import first

conn = sqlite3.connect('Our_data.db')


class Ui_Form(object):
    def setupUi(self, Form):
        self.ekran = Form
        Form.setObjectName("Form")
        Form.resize(833, 439)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 100, 100, 255));")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 461, 391))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid orange;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 170, 311, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit_2.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_2.addWidget(self.dateEdit_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 210, 321, 24))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 30, 321, 24))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_3.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(34, 30, 80, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 30, 233, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(34, 80, 80, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(130, 80, 161, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 110, 161, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_3.setGeometry(QtCore.QRect(130, 140, 161, 21))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_4.setGeometry(QtCore.QRect(130, 170, 161, 21))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_5.setGeometry(QtCore.QRect(130, 200, 161, 21))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_6.setGeometry(QtCore.QRect(130, 230, 161, 21))
        self.radioButton_6.setObjectName("radioButton_6")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(34, 130, 91, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.label_13.setObjectName("label_13")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(130, 130, 221, 22))
        self.lineEdit_10.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(34, 180, 91, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.label_14.setObjectName("label_14")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(130, 230, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius:10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.rent)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 150, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 100, 0);\n"
"border-radius:10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.check)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(130, 180, 221, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.label_15.setText("0")
        self.label_15.setObjectName("label_15")
        self.tabWidget.addTab(self.tab_3, "")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(520, 100, 271, 251))
        self.label_2.setStyleSheet("border-image: url(C:/Users/Fatih/Desktop/final.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200, 70, 70, 255), stop:1 rgba(255, 100, 100, 255));")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Duration Date"))
        self.label_4.setText(_translate("Form", "Passengers"))
        self.label.setText(_translate("Form", "Client Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Rental Order Processed For"))
        self.label_5.setText(_translate("Form", "Plate No"))
        self.label_6.setText(_translate("Form", "Brand"))
        self.radioButton.setText(_translate("Form", "Opel Astra 1.6 Diesel"))
        self.radioButton_2.setText(_translate("Form", "Volkswagen Passat 1.6 TDI"))
        self.radioButton_3.setText(_translate("Form", "Renault Megane 1.5 DCI"))
        self.radioButton_4.setText(_translate("Form", "Opel Astra 1.4 T"))
        self.radioButton_5.setText(_translate("Form", "Volkswagen Golf 1.4 TSI"))
        self.radioButton_6.setText(_translate("Form", "Renault Megane 1.4 T"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Car Rent"))
        self.label_13.setText(_translate("Form", "Tax Amount"))
        self.label_14.setText(_translate("Form", "Total"))
        self.pushButton.setText(_translate("Form", "PAY"))
        self.pushButton_2.setText(_translate("Form", "Check"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Cost Order Summary"))

    def rent(self):
        clientname = self.lineEdit_3.text().format(str)
        date1 = self.dateEdit.text().format(str)
        date2 = self.dateEdit_2.text().format(str)
        passenger = self.lineEdit_4.text().format(str)
        plate = self.lineEdit_2.text().format(str)
        if self.radioButton.isChecked():
            car = "Opel Astra 1.6 Diesel"
        elif self.radioButton_2.isChecked():
            car = "Volkswagen Passat 1.6 TDI"
        elif self.radioButton_3.isChecked():
            car = "Renault Megane 1.5 DCI"
        elif self.radioButton_4.isChecked():
            car = "Opel Astra 1.4 T"
        elif self.radioButton_5.isChecked():
            car = "Volkswagen Golf 1.4 TSI"
        elif self.radioButton_6.isChecked():
            car = "Renault Megane 1.4 T"

        conn.execute('''INSERT INTO RENT(NAME,DATE1, DATE2, PASSENGER, PLATE, CAR) VALUES (?,?,?,?,?,?)''',
                (clientname,date1, date2, passenger, plate, car))
        conn.commit()
        conn.close()

        self.screen = QtWidgets.QMainWindow()
        self.ui = first.Ui_MainWindow()
        self.ui.setupUi(self.screen)
        self.screen.show()
        self.ekran.close()

    def check(self):
        opel1 = 1300
        opel2 = 1000
        vw1 = 1700
        vw2 = 1400
        ren1 = 1000
        ren2 = 900
        total = 0

        tax = self.lineEdit_10.text().format(str)
        if self.radioButton.isChecked():
            total = total + opel1
        elif self.radioButton_2.isChecked():
            total = total + vw1
        elif self.radioButton_3.isChecked():
            total = total + ren1
        elif self.radioButton_4.isChecked():
            total = total + opel2
        elif self.radioButton_5.isChecked():
            total = total + vw2
        elif self.radioButton_6.isChecked():
            total = total + ren2
        else:
            total = total + 0
        self.label_15.setText(total)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
