import json
import mysql.connector
import uuid
import qrcode
import threading
import time
import RPi.GPIO as GPIO

omise_server = 'http://178.128.80.248/'
hold_end_page = 10

cash_box = 40
count = 0
pluse_time = 0

def initialPins():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(cash_box, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(cash_box, GPIO.FALLING, callback=calculateCash, bouncetime=50)
    with open('./room.json', 'r') as f:
        data = json.load(f)
    for item in data:
        GPIO.setup(data[item]['pin'], GPIO.OUT)
        GPIO.output(data[item]['pin'], 0)

def connectDB():
    mydb = mysql.connector.connect(
        host="68.183.227.154",
        user="admin2",
        passwd="192837465",
        database="payment"
    )
    return mydb

def calculateCash(channel):
    global count, pluse_time
    pluse_time = time.time()
    count = count + 1
    # print('Pulse: ' + str(count))

class CheckStatus(threading.Thread):
    def __init__(self, token, ui_mobile, ui_end, home, room_name, door, pin):
        threading.Thread.__init__(self)
        self.token = token
        self.enable = True
        self.mobile_banking = ui_mobile
        self.end = ui_end
        self.home = home
        self.room_name = room_name
        self.door = door
        self.pin = pin
    
    def run(self):
        while self.enable:
            mydb = connectDB()
            mycursor = mydb.cursor()
            querystr = "SELECT pay_status, open_status FROM `payment` WHERE token = '" + self.token + "'"
            mycursor.execute(querystr)
            myresult = mycursor.fetchall()
            pay_status = myresult[0][0]
            open_status = myresult[0][1]
            if pay_status == 1 and open_status == 0:
                self.enable = False
                GPIO.output(self.pin, 1)
                self.mobile_banking.widget.hide()
                self.end.widget.show()
                self.end.label_4.setText(self.room_name)
                self.end.label_6.setText(str(self.door))
                start_time = time.time()
                while time.time() - start_time < hold_end_page:
                    current_time = time.time() - start_time
                    self.end.label_9.setText(str(int(hold_end_page - current_time)))
                    time.sleep(1)
                GPIO.output(self.pin, 0)
                self.end.widget.hide()
                self.home.widget.show()
            time.sleep(2)

class CheckCash(threading.Thread):
    def __init__(self, price, ui_cash, ui_end, home, room_name, door, pin):
        global count, pluse_time
        threading.Thread.__init__(self)
        self.enable = True
        self.ui_cash = ui_cash
        self.end = ui_end
        self.home = home
        self.room_name = room_name
        self.door = door
        self.pin = pin
        self.price = price
        count = 0
        pluse_time = 0

    def run(self):
        global count
        while self.enable:
            if (time.time() - pluse_time > 0.3) and (count != 0):
                cash_bank = 0
                print('Count: ' + str(count))
                if count >= 180 and count <= 220:
                    cash_bank = 1000
                    print("pulse: {}, cash: {}".format(str(count), str(cash_bank)))
                elif count >= 90 and count <= 110:
                    cash_bank = 500
                    print("pulse: {}, cash: {}".format(str(count), str(cash_bank)))
                elif count <= 25 and count > 15:
                    cash_bank = 100
                    print("pulse: {}, cash: {}".format(str(count), str(cash_bank)))
                elif count >= 8 and count < 12:
                    cash_bank = 50
                    print("pulse: {}, cash: {}".format(str(count), str(cash_bank)))
                elif count >= 2 and count < 6:
                    cash_bank = 20
                    print("pulse: {}, cash: {}".format(str(count), str(cash_bank)))
                count = 0
                self.price = self.price - cash_bank
                self.ui_cash.label_4.setText(str(self.price))
                if self.price <= 0 :
                    print('finish')
                    self.enable = False
                    GPIO.output(self.pin, 1)
                    self.ui_cash.widget.hide()
                    self.end.widget.show()
                    self.end.label_4.setText(self.room_name)
                    self.end.label_6.setText(str(self.door))
                    start_time = time.time()
                    while time.time() - start_time < hold_end_page:
                        current_time = time.time() - start_time
                        self.end.label_9.setText(str(int(hold_end_page - current_time)))
                        time.sleep(1)
                    GPIO.output(self.pin, 0)
                    self.end.widget.hide()
                    self.home.widget.show()
            time.sleep(0.1)
 
class RoomManage():
    def __init__(self, room=None):
        with open('./room.json', 'r') as f:
            self.room = json.load(f)
        try:
            self.room_name = room
            self.door = self.room[room]['door']
            self.price = self.room[room]['price']
            self.pin = self.room[room]['pin']
        except:
            self.price = 0
    
    def createQRCode(self, token):
        qrcode.make(omise_server + "?token=" + token).save('qr.png')
    
    def startCash(self, ui_cash, ui_end, ui_home):
        self.ui_cash = ui_cash
        self.end = ui_end
        self.home = ui_home
        self.thread = CheckCash(self.price, self.ui_cash, self.end, self.home, self.room_name, self.door, self.pin)
        self.thread.start()
    
    def stopCash(self):
        self.thread.enable = False
    
    def create_payment(self, ui_mobile, ui_end, ui_home):
        self.mobile_banking = ui_mobile
        self.end = ui_end
        self.home = ui_home
        self.token = str(uuid.uuid4().hex)
        self.createQRCode(self.token)

        mydb = connectDB()
        mycursor = mydb.cursor()
        querystr = "INSERT INTO `payment`(`price`, `token`, `pay_status`, `open_status`) VALUES (%s,%s,%s,%s)"
        val = (str(self.price), self.token, 0, 0)
        mycursor.execute(querystr, val)
        mydb.commit()
        
        self.thread = CheckStatus(self.token, self.mobile_banking, self.end, self.home, self.room_name, self.door, self.pin)
        self.thread.start()
    
    def cancelPayment(self):
        self.thread.enable = False
        mydb = connectDB()
        mycursor = mydb.cursor()
        querystr = "DELETE FROM `payment` WHERE token = '" + self.token + "'"
        mycursor.execute(querystr)
        mydb.commit()


