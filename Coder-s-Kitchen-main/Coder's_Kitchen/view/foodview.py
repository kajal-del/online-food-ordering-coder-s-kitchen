#foodview is module
#food ->Food class object


from model.food import Food
from dbconncetion.myconnection import mycur,conn

class FoodView:
    def addFood(self,food):
        try:
            sqlquery="insert into food(foodname,foodcategory,foodtype,foodprice) values('{}','{}','{}',{})".format(food.getFoodName(),food.getFoodCategory(),food.getFoodType(),food.getFoodPrice())
            print(sqlquery)
            i=mycur.execute(sqlquery)
            print("i:",i)
            conn.commit()
            conn.close()
            if i>0:
                return True
            else:
                return False
        except Exception as e:
            print(e)






    def updateFood(self,food):
        try:
            sqlquery = "update food set foodname='{}',foodcategory='{}',foodtype='{}',foodprice={} where foodid={}".format(
                food.getFoodName(), food.getFoodCategory(), food.getFoodType(), food.getFoodPrice(),food.getFoodId())
            print(sqlquery)
            i = mycur.execute(sqlquery)
            print("i:", i)
            conn.commit()
            conn.close()
            if i > 0:
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def deleteFood(self,foodid):
        try:
            sqlquery = "delete from food where foodid={}".format(foodid)
            print(sqlquery)
            i = mycur.execute(sqlquery)
            print("i:",i)
            conn.commit()
            conn.close()
            if i > 0:
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def showFoodList(self):
        try:
            foodlist = []
            sqlquery = "select *from food"
            foodrows = mycur.execute(sqlquery)
            print("food rows:",foodrows)
            if foodrows>0:
                data=mycur.fetchall() #returns tuple

                for row in data:
                    foodobj=Food(row[0],row[1],row[2],row[3],row[4])
                    foodlist.append(foodobj)
                return foodlist
            else:
                return None
        except Exception as e:
            print(e)

    def searchFoodById(self,foodid):
        try:
            sqlquery = "select *from food where foodid={}".format(foodid)
            foodrows = mycur.execute(sqlquery)
            print("food rows:",foodrows)
            if foodrows>0:
                foodlist=mycur.fetchone()
                return foodlist
            else:
                return None
        except Exception as e:
            print(e)


    def searchFoodByName(self,foodname):
        pass

    def searchFoodByType(self,foodtype):
        pass

    def searchFoodByCategory(self,foodcategory):
        pass