from view.orderview import OrderView
class orderTemplate:
    orderv=OrderView()
    def ordersOperation(self,choice):
        if choice==1:
            print("-----------place order----------")
            custemail=input("Enter email:")
            orderobj=orderTemplate.orderv.placeOrder(custemail)
            print(orderobj)

        if choice==2:
            print("------show My Orders------")
            custemail=input("Enter email:")
            orderlist=orderTemplate.orderv.showMyOrders(custemail)
            for orders in orderlist:
                print(orders)

print("-----Orders-----")
print("1. place order")
print("2. show my orders")
print("3. show all orders")
choice=int(input("Enter choice:"))
orderTemplate().ordersOperation(choice)
