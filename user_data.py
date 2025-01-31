import mysql.connector as mc
import datetime as dt

class userdata:
    conn = mc.connect(host='localhost', user='root', passwd='naresh', database='naresh')
    cur_obj = conn.cursor()
    def every_user_data(self):
        try:
            self.uid = input('enter user id to get user data')
            userdata.cur_obj.execute(f"select date,item,quantity,money from `{self.uid}`")
            print('date    item    quantity    money')
            for i in userdata.cur_obj.fetchall():
                print(f'{i[0]}    {i[1]}    {i[2]}    {i[3]}')
        except mc.DatabaseError as db:
            print('error occured in database is: ',db)

    def all_user_data(self):
        try:
            userdata.cur_obj.execute(f"select uname,uid,phno from musers")
            print('name    user id    ph no')
            for i in userdata.cur_obj.fetchall():
                print(f'{i[0]}    {i[1]}    {i[2]}')
        except mc.DatabaseError as db:
            print('error occured in database is: ',db)



u = userdata()
#u.every_user_data()
u.all_user_data()