import mysql.connector as mc
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class users:
    conn = mc.connect(host='localhost', user='root', passwd='naresh', database='naresh')
    cur_obj = conn.cursor()
    date = dt.date.today()
    def crt_user_table(self):
        try:
            users.cur_obj.execute("create table musers (uname varchar(13),uid varchar(12),passwd varchar(10),phno int)")
            print('milk uesrs table created')
        except mc.DatabaseError as db:
            print('error occurred in database is: ',db)

    def user_register(self):
        try:
            self.uname = input('enter your name: ')
            self.lst2 = []
            users.cur_obj.execute('select uid from musers')
            for i in users.cur_obj.fetchall():
                self.lst2.append(i[0])
            user_id = np.random.randint(10000, 99999)
            self.uid = int(user_id)
            if self.uid not in self.lst2:
                print('user id: ',self.uid)
                self.passwd = input('set a strong password in less than 10 digits: ')
                while 9:
                    self.phno = input('enter your 10 digit phone number: ')
                    if len(self.phno) == 10:
                        users.cur_obj.execute("insert into musers values('%s','%s','%s','%s')" %(self.uname,self.uid,self.passwd,self.phno))
                        users.conn.commit()
                        print('user registered successfully')
                        users.cur_obj.execute(f"create table `{self.uid}` (date varchar(12),item varchar(13),quantity float,money float,tid varchar(13))")
                        break
                    else:
                        print("enter your phone number correctly")
            else:
                print('user id already given ---> try again')
        except mc.DatabaseError as db:
            print('error occurred in database is: ',db)
    @classmethod
    def login(cls):
        users.cur_obj.execute("select uid,passwd from musers")
        lst = []
        lst1 = []
        for i in users.cur_obj.fetchall():
            lst.append(i[0])
            lst1.append(i[1])
        while 9:
            cls.uid = input('enter user id: ')
            cls.passwd = input('enter password: ')
            if cls.uid in lst:
                if cls.passwd in lst1:
                    print('you logged in successfully')
                    break
                else:
                    print('check password --> try again')
            else:
                print('check you user id ---> try again')

    def see_prod(self):
        try:
            lst1 = []
            lst2 = ['Date','Curd','C5kg','C10kg','C1kg','Milk','Ghee','Butter']
            users.cur_obj.execute("select * from mprod where date='%s'" %users.date)
            for i in users.cur_obj.fetchall():
                for j in i:
                    lst1.append(j)
            for i,j in zip(lst2,lst1):
                print(f'{i}      -----> {j}')
        except mc.DatabaseError as db:
            print('error occured in database is: ',db)


    def buy_product(self):
        try:
            while 9:
                self.item = input("enter one item ('curd','milk','ghee','butter') name to buy: ").lower()
                if self.item == 'curd':
                    o.buy_curd()
                    n2 = input('do you want to by curd again(yes/no): ').lower()
                    if n2 == 'no':
                        break
                while 9:
                    self.quatity = float(input("enter how many (kg/L) you want to by: "))
                    users.cur_obj.execute(f"select {self.item} from mprod where date = '{users.date}'")
                    a = 0
                    for i in users.cur_obj.fetchall():
                        a += i[0]
                    b = a-self.quatity
                    if self.quatity < a:
                        users.cur_obj.execute("select cost from prices where item='%s'" %self.item)
                        cst = 0
                        for i in users.cur_obj.fetchall():
                            cst += i[0]
                        self.money= cst*self.quatity
                        print('scan the qr code to pay: ',self.money)
                        h = input('press enter to see qr code:')
                        o.qr_code()
                        users.cur_obj.execute(f"update mprod set {self.item}={b}  where date = '{users.date}'")
                        users.conn.commit()
                        o.every_user_data()
                        break
                    else:
                        print("we don't have that much quantity ---> try less quantity")
                n1 = input('Do you want to by another item(yes/no): ').lower()
                if n1 == 'no':
                    break
        except mc.DatabaseError as db:
            print('error occurred in database is: ',db)
    def qr_code(self):
        image_path = "C:\\Users\\nares\\Downloads\\my_qrcode.jpeg"
        img = mpimg.imread(image_path)
        plt.imshow(img)
        plt.axis('off')  # Hide axes
        plt.show()

    def every_user_data(self):
        users.cur_obj.execute(f"insert into `{users.uid}` (date,item,quantity,money) values('%s','%s',%0.2f,%0.2f)" %(users.date,self.item,self.quatity,self.money))
        users.conn.commit()

    def buy_curd(self):
        try:
            self.quatity = float(input("enter how many (kg/L) you want to by: "))
            self.bucket = input("which bucket u want(c5kg/c10kg/c1kg): ")
            num = int(input('how many buckets u wnat: '))
            users.cur_obj.execute(f"select {self.bucket} from mprod where date = '{users.date}'")
            bks = 0
            for i in users.cur_obj.fetchall():
                print(i[0])
                bks += i[0]
                print(bks)
            self.buket = bks - num
            users.cur_obj.execute(f"update mprod set {self.bucket}={self.buket}  where date = '{users.date}'")
            users.cur_obj.execute(f"select {self.item} from mprod where date = '%s'" %users.date)
            a = 0
            for i in users.cur_obj.fetchall():
                a += i[0]
            b = a-self.quatity
            users.cur_obj.execute(f"update mprod set {self.item}={b}  where date = '%s'" %users.date)
            users.conn.commit()
            if self.quatity < a:
                users.cur_obj.execute("select cost from prices where item='%s'" % self.item)
                cst = 0
                for i in users.cur_obj.fetchall():
                    cst += i[0]
                self.money = cst * self.quatity
                print('scan the qr code to pay: ', self.money)
                h = input('press enter to see qr code:')
                o.qr_code()
                users.cur_obj.execute(f"update mprod set {self.item}={b}  where date = '{users.date}'")
                users.conn.commit()
                o.every_user_data()
            else:
                print("we don't have that much quantity ---> try less quantity")
        except mc.DatabaseError as db:
            print('error occurred in database is: ',db)




o = users()
print('''1 ---> user registration''')
n = input('enter 1 to register, or press enter to login: ')
if n == '1':
    o.user_register()

o.login()
while 9:
    print('''
    2 ---> see items           3 ---> buy items
    4 ---> to exit ''')
    n = input('enter above numbers correctly for corresponding operations: ')
    if n == '2':
        o.see_prod()
    elif n == '3':
        o.see_prod()
        o.buy_product()
    elif n == '4':
        break
