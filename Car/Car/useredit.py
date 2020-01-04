# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'useredit.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(852, 470)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 100, 0, 255), stop:1 rgba(255, 200, 0, 255));")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(390, 50, 101, 101))
        self.label.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/person.png);\n"
"background-color: rgb(170, 255, 255);\n"
"border: 3px solid black;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(120, 50, 181, 31))
        self.textEdit.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 110, 181, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(120, 170, 181, 31))
        self.textEdit_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(120, 230, 181, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 41, 16))
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
        self.textEdit_5.setGeometry(QtCore.QRect(120, 290, 181, 101))
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
        self.pushButton.setText(_translate("Form", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
