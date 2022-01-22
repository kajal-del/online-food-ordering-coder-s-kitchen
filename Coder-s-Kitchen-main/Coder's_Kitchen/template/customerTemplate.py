from view.customerview import CustomerView
from model.customer import Customer

class CustomerTemplate:
    custv=CustomerView()
    def customerOperation(self,choice):
        if choice==1:
            print("----------add customer------------")
            cname=input("Enter Name:")
            cemail=input("Enter Email id:")
            ccont=input("Enter contact:")
            cadd=input("Enter Address:")
            cpass=input("Enter password:")
            ccpass=input("Please re-enter password:")
            if cpass==ccpass:
                custobj=Customer(custname=cname,custemail=cemail,custcontact=ccont,custaddress=cadd,custpassword=cpass,custconfirmpassword=ccpass)
                ans=CustomerTemplate().custv.addCustomer(custobj)
                if ans:
                     print("customer details added successfullly")#registration process
                else:
                    print("customer details not added")
            else:
                print("password and confirm password doesnt match. please try again")

        if choice==4:
            print("----------customer list----------")
            custlist=CustomerTemplate().custv.showCustomerList()
            if custlist!=None:
                for cust in custlist:
                    print(cust)
            else:
                print("No records found")

print("-------Customer--------")

print(" 1. Add Customer")
print(" 2. Update Customer")
print(" 3. Delete Customer")
print(" 4. Show Customer List")
print(" 5. Search Customer By Id")
print(" 6. Search Customer By Email id")

choice=int(input("Enter choice:"))
custt=CustomerTemplate()
custt.customerOperation(choice)