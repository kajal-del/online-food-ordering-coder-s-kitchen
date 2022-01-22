from dbconncetion.myconnection import conn,mycur
from model.cart import Cart
#

class CartView:
    def addToCart(self,cart):
        try:
            print("in")

            sqlquery="insert into cart(foodid,custemail,foodquantity)values({},'{}',{})".format(cart.getFoodId(),cart.getCustEmail(),cart.getFoodQuantity())
            print(sqlquery)
            i=mycur.execute(sqlquery)
            if i>0:
                conn.commit()
                conn.close()
                return True
            else:
                return False
        except Exception as e:
            print(e)
    def deletefromCart(self,cartid):
        pass

    def showMyCart(self,custemail):
        try:
            print("in")
            mycartlist=[]
            sqlquery = "select cartid,foodname,foodcategory,foodtype,foodprice,custemail,foodquantity from cart c inner join food f on c.foodid=f.foodid where custemail='{}'".format(custemail)
            print(sqlquery)
            i = mycur.execute(sqlquery)
            if i > 0:
                data=mycur.fetchall()
                for row in data:
                    cartobj=Cart(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                    mycartlist.append(cartobj)
                return mycartlist
            else:
                return None
        except Exception as e:
            print(e)


