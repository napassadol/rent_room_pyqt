# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/payment.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui__payment(object):
    def setupUi(self, _payment):
        _payment.setObjectName("_payment")
        _payment.resize(1280, 800)
        self.widget = QtWidgets.QWidget(_payment)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(90, 30, 921, 90))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(1020, 50, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setGeometry(QtCore.QRect(160, 700, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setGeometry(QtCore.QRect(770, 700, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(80, 140, 500, 550))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../payment_1.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(700, 140, 500, 550))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../payment_2.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(_payment)
        QtCore.QMetaObject.connectSlotsByName(_payment)

    def retranslateUi(self, _payment):
        _translate = QtCore.QCoreApplication.translate
        _payment.setWindowTitle(_translate("_payment", "Form"))
        self.label_4.setText(_translate("_payment", "เลือกชำระด้วยเงินสดหรือ Mobile Banking"))
        self.pushButton_8.setText(_translate("_payment", "กลับ"))
        self.pushButton_9.setText(_translate("_payment", "เลือกชำระด้วยเงินสด"))
        self.pushButton_10.setText(_translate("_payment", "เลือกชำระด้วย Mobile Banking"))


