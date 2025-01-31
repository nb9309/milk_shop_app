import mysql.connector as mc
import datetime as dt

class app:
    conn = mc.connect(host='localhost',user='root',passwd='naresh',database='naresh')
    cur_obj = conn.cursor()
    date = dt.date.today()
    def crt_table(self):
        try:
            app.cur_obj.execute('create table mprod (date varchar(13), curd int,c5kg int, c10kg int, c1kg int, milk int, ghee int, butter int)')
            print('table created')
        except mc.DatabaseError as db:
            print('error occured in database is: ',db)
    def entr_data(self):
        try:
            app.cur_obj.execute("select date from mprod")
            lst = []
            for i in app.cur_obj.fetchall():
                for j in i:
                    lst.append(j)
            if str(app.date) in lst:
                print('meeru ee roju data already eccharu, so select update option')
            else:
                self.curd = float(input('curd anthaundho enter chayyandi: '))
                self.c5kg = int(input('5kg buckets antha unnayo enter chayyandi: '))
                self.c10kg = int(input('10kg buckets antha unnayo enter chayyandi: '))
                self.c1kg = int(input('1kg packets antha unnayo enter chayyandi: '))
                self.milk = float(input('enter amount of milk: '))
                self.ghee = float(input('enter amount of ghee: '))
                self.butter = float(input('enter amount of butter: '))
                app.cur_obj.execute("insert into mprod (date,curd,c5kg,c10kg,c1kg,milk,ghee,butter) values('%s',%0.2f,%d,%d,%d,%0.2f,%0.2f,%0.2f)" %(app.date,self.curd,self.c5kg,self.c10kg,self.c1kg,self.milk,self.ghee,self.butter))
                app.conn.commit()
                print('data inserted')
        except mc.DatabaseError as db:
            print('error occured in database is: ',db)
        except ValueError:
            print('enter only numbers')

    def update_curd_data(self):
        try:
            app.cur_obj.execute("select curd,c5kg,c10kg,c1kg from mprod where date='%s'" % app.date)
            a = 0
            for i in app.cur_obj.fetchall():
                a += i[0]
                print(f"already unna curd: {i[0]}kg")
                print(f"already unna 5kg buckets: {i[1]}")
                print(f"already unna 10kg buckets: {i[2]}")
                print(f"already unna 1kg buckets: {i[3]}")
            cur = float(input('enter amount of butter: '))
            self.curd = a + cur
            self.c5kg = int(input('motham 5kg buckets antha unnayo enter chayyandi: '))
            self.c10kg = int(input('motham over all 10kg buckets antha unnayo enter chayyandi: '))
            self.c1kg = int(input('motham 1kg packets antha unnayo enter chayyandi: '))
            app.cur_obj.execute("update mprod set curd= %0.2f, c5kg = %d, c10kg= %d, c1kg = %d where date='%s'" %(self.curd,self.c5kg,self.c10kg,self.c1kg,app.date))
            app.conn.commit()
            print('curd data updated')
        except mc.DatabaseError as db:
            print('error occured in database is: ',db)
        except ValueError:
            print('enter only numbers')

    def update_milk(self):
        try:
            app.cur_obj.execute("select milk from mprod where date='%s'" % app.date)
            a = 0
            for i in app.cur_obj.fetchall():
                a += i[0]
                print(f'already unna milk: {i[0]}kg')
            mil = float(input('enter amount of milk: '))
            self.milk = a + mil
            app.cur_obj.execute("update mprod set milk=%0.2f where date='%s'" %(self.milk,app.date))
            app.conn.commit()
            print('milk data updated')
        except mc.DatabaseError as db:
            print('error occured in database is: ',db)
        except ValueError:
            print('enter only numbers')

    def update_ghee(self):
        try:
            app.cur_obj.execute("select ghee from mprod where date='%s'" %app.date)
            a = 0
            for i in app.cur_obj.fetchall():
                a += i[0]
                print(f'already unna ghee: {i[0]}kg')
            ghe = float(input('enter amount of ghee: '))
            self.ghee=a+ghe
            app.cur_obj.execute("update mprod set ghee=%0.2f where date='%s'" %(self.ghee,app.date))
            app.conn.commit()
            print('ghee data updated')
        except mc.DatabaseError as db:
            print('error occured in database is: ',db)
        except ValueError:
            print('enter only numbers')

    def update_butter(self):
        try:
            app.cur_obj.execute("select butter from mprod where date='%s'" %app.date)
            a = 0
            for i in app.cur_obj.fetchall():
                a += i[0]
                print(f'already unna butter: {i[0]}kg')
            buter= float(input('enter amount of butter: '))
            self.butter=a+buter
            app.cur_obj.execute("update mprod set butter=%0.2f where date='%s'" % (self.butter, app.date))
            app.conn.commit()
            print('butter data updated')
        except mc.DatabaseError as db:
            print('error occured in database is: ',db)
        except ValueError:
            print('enter only numbers')

    def see_data(self):
        try:
            lst1 = []
            lst2 = ['Date','Curd','C5kg','C10kg','C1kg','Milk','Ghee','Butter']
            app.cur_obj.execute("select * from mprod where date='%s'" %app.date)
            for i in app.cur_obj.fetchall():
                for j in i:
                    lst1.append(j)
            for i,j in zip(lst2,lst1):
                print(f'{i}      -----> {j}')
        except mc.DatabaseError as db:
            print('error occured in database is: ',db)


s = app()
while 9:
    print(''' 
    1 ---> to enter amount of curd, milk, ghee, butter    2 ---> to update curd data
    3 ---> to update milk data                            4 ---> to update ghee data
    5 ---> to update butter data                          6 ---> prastutham unna products chudataniki
    7 ---> process apadaniki''')
    n = input('paina panulu chayyadaniki correct number enter chayyandi: ')
    if n == '1':
        s.entr_data()
    elif n == '2':
        s.update_curd_data()
    elif n == '3':
        s.update_milk()
    elif n == '4':
        s.update_ghee()
    elif n == '5':
        s.update_butter()
    elif n == '6':
        s.see_data()
    elif n == '7':
        break