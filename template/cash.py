# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/cash.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cash_2(object):
    def setupUi(self, cash_2):
        cash_2.setObjectName("cash_2")
        cash_2.resize(1240, 800)
        self.widget = QtWidgets.QWidget(cash_2)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(90, 30, 730, 90))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(960, 30, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(800, 270, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(690, 330, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(800, 330, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(80, 140, 500, 550))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../cash.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(970, 330, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(cash_2)
        QtCore.QMetaObject.connectSlotsByName(cash_2)

    def retranslateUi(self, cash_2):
        _translate = QtCore.QCoreApplication.translate
        cash_2.setWindowTitle(_translate("cash_2", "Form"))
        self.label.setText(_translate("cash_2", "ชำระด้วยเงินสด"))
        self.pushButton.setText(_translate("cash_2", "กลับ"))
        self.label_2.setText(_translate("cash_2", "จำนวนเงิน"))
        self.label_3.setText(_translate("cash_2", "คงเหลือ"))
        self.label_4.setText(_translate("cash_2", "0"))
        self.label_6.setText(_translate("cash_2", "บาท"))


