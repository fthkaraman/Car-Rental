# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'policy.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import first


class Ui_Form(object):
    def setupUi(self, Form):
        self.ekran =Form
        Form.setObjectName("Form")
        Form.resize(830, 436)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(100, 200, 40, 255), stop:1 rgba(100, 100, 255, 255));")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(120, 70, 581, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(420, 70, 141, 131))
        self.label.setStyleSheet("border-image: url(C:/Users/Fatih/Desktop/smoke.png);\n"
"background-color: rgb(100, 100, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(30, 40, 331, 221))
        self.textEdit.setStyleSheet("background-color: rgb(100, 200, 40);")
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(340, 70, 221, 131))
        self.label_2.setStyleSheet("border-image: url(C:/Users/Fatih/Desktop/border.png);\n"
"background-color: rgb(100, 100, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 30, 331, 221))
        self.textEdit_2.setStyleSheet("background-color: rgb(100, 200, 40);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(310, 20, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 380, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 100, 0);\n"
"border-radius:10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.first)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Custom-Demi,Arial,sans-serif\'; font-size:14pt; font-weight:600; color:#333333; background-color:#ffffff;\">No, smoking is not allowed in rental cars</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Custom-Regular,Arial,sans-serif\'; font-size:14pt; color:#333333; background-color:#ffffff;\">.We began this </span><a href=\"https://www.avis.com/en/customer-service/faqs/usa/avis-car-sales/non-smoking\"><span style=\" font-family:\'Custom-Regular,Arial,sans-serif\'; font-size:14pt; text-decoration: underline; color:#d4002a; background-color:#ffffff;\">non-smoking policy</span></a><span style=\" font-family:\'Custom-Regular,Arial,sans-serif\'; font-size:14pt; color:#333333; background-color:#ffffff;\"> on October 1, 2009, to ensure that all our customers drive in a comfortable, clean car. A cleaning fee of up to $250 may be applied to the cost of a rental, should this non-smoking policy be violated.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Smoking"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,Verdana,sans-serif\'; font-size:8pt; font-weight:600; color:#424345;\">Driving rental car from Turkey to Greece or Europe:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Arial,Verdana,sans-serif\'; font-size:8pt; color:#292929;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">Vehicles rented in Turkey can be driven throughout Europe.<br /><br /></span></li>\n"
"<li style=\" font-family:\'Arial,Verdana,sans-serif\'; font-size:8pt; color:#292929;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">Vehicles cannot be driven into Greece.</span></li></ul></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Border"))
        self.lineEdit.setText(_translate("Form", "Our Policies"))
        self.pushButton_2.setText(_translate("Form", "Back"))

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
