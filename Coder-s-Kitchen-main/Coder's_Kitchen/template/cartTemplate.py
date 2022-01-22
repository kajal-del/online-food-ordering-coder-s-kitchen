from view . foodview import FoodView
from view . cartview import CartView
from model.cart import Cart
class CartTemplate:
    cartv=CartView()
    def cartOperation(self,choice):
        if choice==1:
            print("--------Add to Cart-------")
            foodlist=FoodView().showFoodList()
            for food in foodlist:
                print(food)
            fid=int(input("Enter food id:"))
            cemail=input("Enter email:")
            foodq=int(input("Enter food quantity:"))

            cartObj=Cart(foodid=fid,custemail=cemail,foodquantity=foodq)
            ans=CartTemplate.cartv.addToCart(cartObj)

            if ans:
                print("item added in your cart")
            else:
                print("item not added in cart")

        if choice==3:
            print("-----show my cart------")
            cemail=input("Enter email:")
            cartlist=CartTemplate.cartv.showMyCart(cemail)
            if cartlist!=None:
                for cart in cartlist:
                    print(cart)
            else:
                print("No cart list found")
print("-------Cart-------")
print(" 1. Add to Cart")
print(" 2. Delete Cart")
print(" 3. Show My Cart list")
choice=int(input("Enter your choice:"))
CartTemplate().cartOperation(choice)