# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cars.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import first


class Ui_Form(object):
    def setupUi(self, Form):
        self.ekran = Form
        Form.setObjectName("Form")
        Form.resize(806, 460)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200, 100, 0, 255), stop:1 rgba(100, 255, 255, 255));")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(30, 10, 751, 441))
        self.frame_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(200, 150, 0, 255), stop:1 rgba(150, 255, 255, 255));")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setGeometry(QtCore.QRect(20, 10, 191, 191))
        self.frame.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border:3px solid black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 10, 111, 51))
        self.label.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/renault1.png);\n"
"border:3px solid black;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 71, 167, 108))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setGeometry(QtCore.QRect(280, 10, 191, 191))
        self.frame_2.setStyleSheet("background-color: rgb(0, 150, 255);\n"
"border:3px solid black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(40, 10, 111, 61))
        self.label_5.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/passat.png);\n"
"border:3px solid black;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 71, 167, 108))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setGeometry(QtCore.QRect(540, 10, 191, 191))
        self.frame_3.setStyleSheet("background-color: rgb(0, 150, 255);\n"
"border:3px solid black;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(50, 10, 101, 61))
        self.label_9.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/golf.png);\n"
"border:3px solid black;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(11, 71, 167, 108))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(20, 230, 191, 191))
        self.frame_5.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border:3px solid black;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setGeometry(QtCore.QRect(40, 10, 111, 51))
        self.label_13.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/renault1.png);\n"
"border:3px solid black;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.layoutWidget_3 = QtWidgets.QWidget(self.frame_5)
        self.layoutWidget_3.setGeometry(QtCore.QRect(11, 71, 167, 108))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_4.addWidget(self.label_16)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setGeometry(QtCore.QRect(280, 230, 191, 191))
        self.frame_6.setStyleSheet("background-color: rgb(0, 255, 150);\n"
"border:3px solid black;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_17 = QtWidgets.QLabel(self.frame_6)
        self.label_17.setGeometry(QtCore.QRect(50, 10, 101, 61))
        self.label_17.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/astra.png);\n"
"border:3px solid black;")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.layoutWidget_4 = QtWidgets.QWidget(self.frame_6)
        self.layoutWidget_4.setGeometry(QtCore.QRect(11, 71, 167, 108))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_5.addWidget(self.label_20)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.pushButton_5)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setGeometry(QtCore.QRect(540, 230, 191, 191))
        self.frame_7.setStyleSheet("background-color: rgb(0, 255, 150);\n"
"border:3px solid black;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_29 = QtWidgets.QLabel(self.frame_7)
        self.label_29.setGeometry(QtCore.QRect(50, 10, 101, 61))
        self.label_29.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/astra1.png);\n"
"border:3px solid black;")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.layoutWidget_7 = QtWidgets.QWidget(self.frame_7)
        self.layoutWidget_7.setGeometry(QtCore.QRect(11, 71, 167, 108))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_8.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_8.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_8.addWidget(self.label_32)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_8.addWidget(self.pushButton_8)

        self.pushButton.clicked.connect(self.first)
        self.pushButton_2.clicked.connect(self.first)
        self.pushButton_3.clicked.connect(self.first)
        self.pushButton_4.clicked.connect(self.first)
        self.pushButton_5.clicked.connect(self.first)
        self.pushButton_8.clicked.connect(self.first)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Renault Megane"))
        self.label_3.setText(_translate("Form", "Megane JOY 1.5 DCI 75 BG EU6"))
        self.label_4.setText(_translate("Form", "       1000 TL"))
        self.pushButton.setText(_translate("Form", "Check"))
        self.label_6.setText(_translate("Form", "Volkswagen Passat"))
        self.label_7.setText(_translate("Form", "Passat Highline 1.6 TDI DSG"))
        self.label_8.setText(_translate("Form", "       1700 TL"))
        self.pushButton_2.setText(_translate("Form", "Check"))
        self.label_10.setText(_translate("Form", "Volkswagen Golf"))
        self.label_11.setText(_translate("Form", "Golf Comfortline 1.4 TSI DSG"))
        self.label_12.setText(_translate("Form", "       1400 TL"))
        self.pushButton_3.setText(_translate("Form", "Check"))
        self.label_14.setText(_translate("Form", "Renault Megane"))
        self.label_15.setText(_translate("Form", "Megane JOY 1.5 DCI 75 BG EU6"))
        self.label_16.setText(_translate("Form", "       1000 TL"))
        self.pushButton_4.setText(_translate("Form", "Check"))
        self.label_18.setText(_translate("Form", "Opel Astra Sedan"))
        self.label_19.setText(_translate("Form", "Astra Cosmo 1.6 Diesel"))
        self.label_20.setText(_translate("Form", "       1300 TL"))
        self.pushButton_5.setText(_translate("Form", "Check"))
        self.label_30.setText(_translate("Form", "Opel Astra Hatchback"))
        self.label_31.setText(_translate("Form", "Astra Cosmo 1.4 Gasoline"))
        self.label_32.setText(_translate("Form", "       1000 TL"))
        self.pushButton_8.setText(_translate("Form", "Check"))

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
