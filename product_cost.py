import mysql.connector as mc
import datetime as dt

class cost:
    conn = mc.connect(host='localhost', user='root', passwd='naresh', database='naresh')
    cur_obj = conn.cursor()
    date = dt.date.today()
    def cost_table(self):
        try:
            cost.cur_obj.execute("create table prices (date varchar(13),item varchar(13), cost float)")
            print("prices table created")
        except mc.DatabaseError as db:
            print('error occurred in database is: ',db)

    def enter_prices(self):
        try:
            while 9:
                self.item = input("item ('curd','milk','ghee','butter') peru enter chayyandi: ")
                cost.cur_obj.execute("select item from prices")
                lst = []
                for i in cost.cur_obj.fetchall():
                    for j in i:
                        lst.append(j)
                if str(self.item) in lst:
                    print('meeru ee roju data already eccharu, so select update option')
                    break
                else:
                    self.cost = float(input('item cost enter chayyandi: '))
                    cost.cur_obj.execute("insert into prices values('%s','%s',%0.2f)" %(cost.date,self.item,self.cost))
                    print('data entered')
                    cost.conn.commit()
                    n = input('enkoka item enter chaesthara(yes/no): ').lower()
                    if n == 'no':
                        break
        except mc.DatabaseError as db:
            print('error occurred in database is: ',db)

    def up_cost(self):
        try:
            self.item = input("item ('curd','milk','ghee','butter') peru enter chayyandi: ")
            self.cost = float(input('updated cost enter chayyandi: '))
            cost.cur_obj.execute("update prices set cost=%0.2f where item='%s' and date='%s'" %(self.cost,self.item,cost.date))
            cost.conn.commit()
            print('price upadate ayyendhi')
        except mc.DatabaseError as db:
            print('error occurred in database is: ', db)

    def see_prices(self):
        try:
            cost.cur_obj.execute("select item,cost from prices where date='%s'" %cost.date)
            for i in cost.cur_obj.fetchall():
                print(f'{i[0]}(kg/L) ----> {i[1]}')
        except mc.DatabaseError as db:
            print('error occurred in database is: ', db)

obj = cost()
while 9:
    print('''
     1 -----> prices enter chayyadaniki      2 ----> prices update chayyadaniki
     3 -----> prices chudataniki             4 -----> process apadaniki''')
    n = input('paina panulu chayyadaniki correct number nokkandi: ')
    if n == '1':
        obj.enter_prices()
    elif n == '2':
        obj.up_cost()
    elif n == '3':
        obj.see_prices()
    elif n == '4':
        break
