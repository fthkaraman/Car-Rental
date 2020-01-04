# -*- coding: utf-8 -*-

# MainWindow implementation generated from reading ui file 'carrental.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import clientedit
import cars
import filter
import rent
import policy


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.ekran = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 502)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 100, 255, 255), stop:1 rgba(255, 0, 0, 100));")
        self.toolButton = QtWidgets.QToolButton(MainWindow)
        self.toolButton.setGeometry(QtCore.QRect(190, 110, 91, 91))
        self.toolButton.setAutoFillBackground(False)
        self.toolButton.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/user.png);\n"
"\n"
"\n"
"\n"
"")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.policy)
        self.toolButton_2 = QtWidgets.QToolButton(MainWindow)
        self.toolButton_2.clicked.connect(self.clientedit)
        self.toolButton_2.setGeometry(QtCore.QRect(400, 110, 91, 91))
        self.toolButton_2.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/client.png);\n"
"\n"
"")
        self.toolButton_2.setText("")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(MainWindow)
        self.toolButton_3.clicked.connect(self.cars)
        self.toolButton_3.setGeometry(QtCore.QRect(620, 110, 91, 91))
        self.toolButton_3.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/cars.png);\n"
"")
        self.toolButton_3.setText("")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(MainWindow)
        self.toolButton_4.clicked.connect(self.filter)
        self.toolButton_4.setGeometry(QtCore.QRect(190, 310, 91, 91))
        self.toolButton_4.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/filter.png);\n"
"")
        self.toolButton_4.setText("")
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(MainWindow)
        self.toolButton_5.setGeometry(QtCore.QRect(400, 310, 91, 91))
        self.toolButton_5.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/cars.png);\n"
"")
        self.toolButton_5.setText("")
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_5.clicked.connect(self.rent)
        self.toolButton_6 = QtWidgets.QToolButton(MainWindow)
        self.toolButton_6.setGeometry(QtCore.QRect(620, 310, 91, 91))
        self.toolButton_6.setStyleSheet("background-image:url(C:/Users/Fatih/Desktop/logout.png);\n"
"")
        self.toolButton_6.setText("")
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_6.clicked.connect(self.ekran.close)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(190, 210, 91, 21))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("QLabel{background-color: rgb(255, 255, 255)};\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(400, 210, 91, 21))
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setStyleSheet("QLabel{background-color: rgb(255, 255, 255)}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(620, 210, 91, 21))
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setStyleSheet("QLabel{background-color: rgb(255, 255, 255)}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(190, 410, 91, 21))
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setStyleSheet("QLabel{background-color: rgb(255, 255, 255)}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(400, 410, 91, 21))
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setStyleSheet("QLabel{background-color: rgb(255, 255, 255)}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(620, 410, 91, 21))
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setStyleSheet("QLabel{background-color: rgb(255, 255, 255)}")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "           About"))
        self.label_2.setText(_translate("MainWindow", "           Client"))
        self.label_3.setText(_translate("MainWindow", "           Cars"))
        self.label_4.setText(_translate("MainWindow", "           Filter"))
        self.label_5.setText(_translate("MainWindow", "        Rent Car"))
        self.label_6.setText(_translate("MainWindow", "         Log Out"))

    def clientedit(self):
        self.screen = QtWidgets.QWidget()
        self.ui = clientedit.Ui_Form()
        self.ui.setupUi(self.screen)
        self.screen.show()
        self.ekran.close()

    def cars(self):
        self.screen = QtWidgets.QWidget()
        self.ui = cars.Ui_Form()
        self.ui.setupUi(self.screen)
        self.screen.show()
        self.ekran.close()

    def filter(self):
        self.screen = QtWidgets.QWidget()
        self.ui = filter.Ui_Form()
        self.ui.setupUi(self.screen)
        self.screen.show()
        self.ekran.close()

    def rent(self):
        self.screen = QtWidgets.QWidget()
        self.ui = rent.Ui_Form()
        self.ui.setupUi(self.screen)
        self.screen.show()
        self.ekran.close()

    def policy(self):
        self.screen = QtWidgets.QWidget()
        self.ui = policy.Ui_Form()
        self.ui.setupUi(self.screen)
        self.screen.show()
        self.ekran.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
