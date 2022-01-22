
class Cart:
    def __init__(self,cartid=0,foodid=0,foodname=None,foodcategory=None,foodtype=None,foodprice=0,custemail=None,foodquantity=0):

        self.cartid=cartid
        self.foodid = foodid
        self.foodname = foodname
        self.foodcategory = foodcategory
        self.foodtype = foodtype
        self.foodprice = foodprice
        self.custemail=custemail
        self.foodquantity=foodquantity

    def setCartId(self,cartid):
        self.cartid=cartid

    def getCartId(self):
        return self.cartid

    def setCustEmail(self,custemail):
        self.custemail=custemail

    def getCustEmail(self):
        return self.custemail

    def setFoodQuantity(self, foodquantity):
        self.foodquantity = foodquantity

    def getFoodQuantity(self):
        return self.foodquantity

    def setFoodId(self, foodid):
        self.foodid = foodid

    def getFoodId(self):
        return self.foodid

    def setFoodName(self, foodname):
        self.foodname = foodname

    def getFoodName(self):
        return self.foodname

    def setFoodCategory(self, foodcategory):
        self.foodcategory = foodcategory

    def getFoodCategory(self):
        return self.foodcategory

    def setFoodType(self, foodtype):
        self.foodtype = foodtype

    def getFoodType(self):
        return self.foodtype

    def setFoodPrice(self, foodprice):
        self.foodprice = foodprice

    def getFoodPrice(self):
        return self.foodprice

    def __str__(self):
        return "cart[cartid={},foodid={},foodname={},foodcategory={},foodtype={},foodprice={},custemail={},foodquantity={}]".format(self.cartid,self.foodid,self.foodname,self.foodcategory,self.foodtype,self.foodprice,self.custemail,self.foodquantity)
