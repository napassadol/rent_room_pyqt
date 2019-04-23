import sys
import qrcode
import json

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from template.home import Ui_Form as Ui_home
from template.select_room import Ui_Form as Ui_select_room
from template.payment import Ui__payment as Ui_payment
from template.cash import Ui_cash_2 as Ui_cash
from template.mobile_banking import Ui_Form as Ui_mobile_banking
from template.end import Ui_Form as Ui_end

from room import RoomManage, initialPins

class MyApp(QMainWindow):
    room_manage = RoomManage()
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.home = Ui_home()
        self.home.setupUi(self)

        self.select_room = Ui_select_room()
        self.select_room.setupUi(self)
        self.select_room.widget.hide()

        self.payment = Ui_payment()
        self.payment.setupUi(self)
        self.payment.widget.hide()

        self.cash = Ui_cash()
        self.cash.setupUi(self)
        self.cash.widget.hide()

        self.mobile_banking = Ui_mobile_banking()
        self.mobile_banking.setupUi(self)
        self.mobile_banking.widget.hide()

        self.end = Ui_end()
        self.end.setupUi(self)
        self.end.widget.hide()

        self.initButton()
        self.initLabel()
        initialPins()

    def homeButton(self):
        # self.home.widget.mouseDoubleClickEvent = lambda event:self.openHome()
        self.home.pushButton.clicked.connect(lambda :self.openHome())
    
    def selectRoomButton(self):
        self.select_room.pushButton_2.clicked.connect(self.home.widget.show)
        self.select_room.pushButton_2.clicked.connect(self.select_room.widget.hide)
        # with open('./room.json', 'r') as f:
        #     data = json.load(f)
        # for item in data:
        #     if data[item]['sequence'] == 0:
        #         self.select_room.pushButton_3.clicked.connect(lambda: self.selectRoom(item))
        #         self.select_room.pushButton_3.setText(data[item]['buttonText'])
        #     if data[item]['sequence'] == 1:
        #         self.select_room.pushButton_4.clicked.connect(lambda: self.selectRoom(item))
        #         self.select_room.pushButton_4.setText(data[item]['buttonText'])
        #     if data[item]['sequence'] == 2:
        #         self.select_room.pushButton_5.clicked.connect(lambda: self.selectRoom(item))
        #         self.select_room.pushButton_5.setText(data[item]['buttonText'])
        #     if data[item]['sequence'] == 3:
        #         self.select_room.pushButton_6.clicked.connect(lambda: self.selectRoom(item))
        #         self.select_room.pushButton_6.setText(data[item]['buttonText'])
        self.select_room.pushButton_3.clicked.connect(lambda: self.selectRoom('A'))
        self.select_room.pushButton_4.clicked.connect(lambda: self.selectRoom('B'))
        self.select_room.pushButton_5.clicked.connect(lambda: self.selectRoom('C'))
        self.select_room.pushButton_6.clicked.connect(lambda: self.selectRoom('D'))
    
    def paymentButton(self):
        self.payment.pushButton_8.clicked.connect(self.select_room.widget.show)
        self.payment.pushButton_8.clicked.connect(self.payment.widget.hide)

        self.payment.pushButton_9.clicked.connect(lambda: self.openCash())

        self.payment.pushButton_10.clicked.connect(lambda: self.openMobileBanking())
    
    def cashButton(self):
        # self.cash.pushButton.clicked.connect(self.cash.widget.hide)
        # self.cash.pushButton.clicked.connect(self.payment.widget.show)
        self.cash.pushButton.clicked.connect(lambda: self.cloasCash())
    
    def mobilrBankingButton(self):
        self.mobile_banking.pushButton.clicked.connect(lambda: self.closeMobileBanking())

    def initButton(self):
        self.homeButton()
        self.selectRoomButton()
        self.paymentButton()
        self.cashButton()
        self.mobilrBankingButton()
    
    def endLabel(self):
        self.end.label_7.setPixmap(QtGui.QPixmap('end.png'))
        self.end.label_7.setScaledContents(True)
    
    def paymentLabel(self):
        self.payment.label_5.setPixmap(QtGui.QPixmap('payment_1.png'))
        self.payment.label_5.setScaledContents(True)

        self.payment.label_6.setPixmap(QtGui.QPixmap('payment_2.png'))
        self.payment.label_6.setScaledContents(True)

    def cashLabel(self):
        self.cash.label_4.setText(str(self.room_manage.price))
        self.cash.label_5.setPixmap(QtGui.QPixmap('cash.png'))
        self.cash.label_5.setScaledContents(True)
    
    def mobileBankingLabel(self):
        self.mobile_banking.label_3.setText(str(self.room_manage.price))
        self.mobile_banking.label_9.setPixmap(QtGui.QPixmap('mobile_banking.png'))
        self.mobile_banking.label_9.setScaledContents(True)
    
    def homeLabel(self):
        self.home.label_3.setPixmap(QtGui.QPixmap('home.png'))
        self.home.label_3.setScaledContents(True)
    
    def selectRoomLabet(self):
        self.select_room.label_4.setPixmap(QtGui.QPixmap('select room.png'))
        self.select_room.label_4.setScaledContents(True)
    
    def openHome(self):
        self.home.widget.hide()
        self.select_room.widget.show()
    
    def initLabel(self):
        self.homeLabel()
        self.selectRoomLabet()
        self.cashLabel()
        self.mobileBankingLabel()
        self.paymentLabel()
        self.endLabel()

    def selectRoom(self, room=None):
        self.room_manage = RoomManage(room)
        self.select_room.widget.hide()
        self.payment.widget.show()
        print('Room: ' + str(room))
        self.cashLabel()
    
    def openCash(self):
        self.payment.widget.hide()
        self.cash.widget.show()
        self.room_manage.startCash(self.cash, self.end, self.home)
    
    def cloasCash(self):
        self.cash.widget.hide()
        self.payment.widget.show()
        self.room_manage.stopCash()

    
    def openMobileBanking(self):
        self.payment.widget.hide()
        self.mobile_banking.widget.show()
        self.room_manage.create_payment(self.mobile_banking, self.end, self.home)
        self.mobile_banking.label_8.setPixmap(QtGui.QPixmap('qr.png'))
        self.mobile_banking.label_8.setScaledContents(True)
        self.mobileBankingLabel()

    def closeMobileBanking(self):
        self.room_manage.cancelPayment()
        self.mobile_banking.widget.hide()
        self.payment.widget.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
