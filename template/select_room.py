# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/select_room.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 800)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(90, 30, 731, 91))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(960, 50, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 140, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 220, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(710, 300, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(710, 380, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(710, 460, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(90, 140, 550, 600))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../select room.png"))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "โปรดเลือกห้องพัก"))
        self.pushButton_2.setText(_translate("Form", "กลับ"))
        self.pushButton_3.setText(_translate("Form", "เลือกห้อง A"))
        self.pushButton_4.setText(_translate("Form", "เลือกห้อง B"))
        self.pushButton_5.setText(_translate("Form", "เลือกห้อง C"))
        self.pushButton_6.setText(_translate("Form", "เลือกห้อง D"))
        self.pushButton_7.setText(_translate("Form", "เลือกห้อง E"))


