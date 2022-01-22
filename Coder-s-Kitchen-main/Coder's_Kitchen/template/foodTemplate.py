#from pack.nodulename import classname
from model.food import Food
from view.foodview import FoodView

class FoodTemplate:

    foodv=FoodView() #class variable

    def foodOperations(self,choice):
        if choice==1:
            print("-------Add Food Operation-----")
            fname=input("Enter Food name:")
            fcategory=input("Enter food category:")
            ftype=input("Enter Food Type:")
            fprice=int(input("Enter Food Price:"))
            food=Food(foodname=fname,foodcategory=fcategory,foodtype=ftype,foodprice=fprice)
            ans=FoodTemplate.foodv.addFood(food)
            if ans:
                print("Food is added successfully")
            else:
                print("Food not added. :-( please try again")

        if choice==2:
            print("-------Update Food Operation-----")

            foodlist=FoodTemplate.foodv.showFoodList()
            print(foodlist)
            if foodlist!=None:
                fname = input("Enter Food name:")
                fcategory = input("Enter food category:")
                ftype = input("Enter Food Type:")
                fprice = int(input("Enter Food Price:"))
                fid=int(input("Enter food id:"))
                food = Food(foodname=fname, foodcategory=fcategory, foodtype=ftype, foodprice=fprice,foodid=fid)
                ans = FoodTemplate.foodv.updateFood(food)
                if ans:
                    print("Food is updated successfully")
                else:
                    print("Food not updated. :-( please try again")
        if choice==3:
            print("-------delete food--------")
            foodlist=FoodTemplate.foodv.showFoodList()
            if foodlist!=None:
                print(foodlist)
                foodid=int(input("Enter Food id:"))
                ans=FoodTemplate.foodv.deleteFood(foodid)
                if ans:
                    print("food deleted")

                else:
                    print("food not deleted. :-( please try again")
            else:
                print("No food Records found to delete")
        if choice==4:
            print("--------show food list-----------")
            foodlist=FoodTemplate.foodv.showFoodList()


            if foodlist!=None:
                for food in foodlist:   #food is nothing but Food class Object
                    print(food)
            
            else:
                print("No food Records found")

        if choice==5:
            print("----search food by id----")
            fid=int(input("Enter food id:"))
            foodlist=FoodTemplate.foodv.searchFoodById(fid)
            if foodlist!=None:
                print(foodlist)
            else:
                print("no food record found with {} id".format(fid))




print("==============Welcome to Coder's kitchen===============")
print("-"*30)
print(" 1.Add Food")
print(" 2.Update Food")
print(" 3.Delete Food")
print(" 4.Show food list")
print(" 5.search food by id")
choice=int(input("Enter Choice:"))
foodt=FoodTemplate()
foodt.foodOperations(choice)


