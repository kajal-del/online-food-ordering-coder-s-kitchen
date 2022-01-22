#food -module(any python file)
'''
mysql> create database coders_kitchen
    -> ;
Query OK, 1 row affected (0.61 sec)

create table food
    (foodid int primary key auto_increment,
    foodname varchar(100) not null,
    foodcategory varchar(100) not null,
    foodtype varchar(100) not null,
    foodprice int not null)
    ;

'''
class Food:

    def __init__(self,foodid=0,foodname=None,foodcategory=None,foodtype=None,foodprice=0):
        self.foodid=foodid
        self.foodname=foodname
        self.foodcategory=foodcategory
        self.foodtype=foodtype
        self.foodprice=foodprice


    def setFoodId(self,foodid):
        self.foodid=foodid

    def getFoodId(self):
        return self.foodid

    def setFoodName(self,foodname):
        self.foodname=foodname

    def getFoodName(self):
        return self.foodname

    def setFoodCategory(self,foodcategory):
        self.foodcategory=foodcategory

    def getFoodCategory(self):
        return self.foodcategory

    def setFoodType(self,foodtype):
        self.foodtype=foodtype

    def getFoodType(self):
        return self.foodtype

    def setFoodPrice(self,foodprice):
        self.foodprice=foodprice

    def getFoodPrice(self):
        return self.foodprice


    def __str__(self):
        return "Food[foodid={},foodname={},foodcategory={},foodtype={},foodprice={}]".format(self.foodid,self.foodname,self.foodcategory,self.foodtype,self.foodprice)