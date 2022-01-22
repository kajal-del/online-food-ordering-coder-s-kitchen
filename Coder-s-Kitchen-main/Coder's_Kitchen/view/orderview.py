import datetime
from dbconncetion.myconnection import mycur,conn
from model.orders import Orders
class OrderView:
    def placeOrder(self,custemail):
        try:
            orderdate=datetime.date.today()
            print(orderdate)
            sqlquery1=" select sum(foodprice*foodquantity) as 'totalprice' from food inner join cart on food.foodid=cart.foodid where custemail='{}'".format(custemail)
            i=mycur.execute(sqlquery1) #i=1
            row=mycur.fetchone()
            totalprice=row[0]
            print("total price:",totalprice)
            sqlquery2="insert into orders(custemail,orderdate,totalprice)value('{}','{}',{})".format(custemail,orderdate,totalprice)
            print(sqlquery2)
            i=mycur.execute(sqlquery2)
            conn.commit()
            if i>0:
               sqlq="delete from cart where custemail='{}'".format(custemail)
               mycur.execute(sqlq)
               conn.commit()
               sqlquery3="select *from orders where custemail='{}' and orderdate='{}'".format(custemail,orderdate)
               i=mycur.execute(sqlquery3)
            if i>0:
                    row=mycur.fetchone()
                    orderobj=Orders(row[0],row[1],row[2],row[3],row[4])
                    return orderobj
            else:
                return None
        except Exception as e:
            print(e)


    def showMyOrders(self,custemail):
        try:
            orderlist=[]
            sqlquery3 = "select *from orders where custemail='{}'".format(custemail)
            i = mycur.execute(sqlquery3)

            if i > 0:
                data=mycur.fetchall()
                for row in data:
                    orderob=Orders(row[0],row[1],row[2],row[3],row[4])
                    orderlist.append(orderob)
                return orderlist
        except Exception as e:
            print(e)


    def showAllOrder(self):
        pass
        #hw