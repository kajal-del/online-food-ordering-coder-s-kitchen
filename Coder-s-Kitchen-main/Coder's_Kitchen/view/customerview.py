from dbconncetion.myconnection import mycur,conn
from model.customer import Customer
class CustomerView:

    def addCustomer(self,customer):

        try:
            sqlquary="insert into customer(custname,custemail,custcontact,custaddress,custpassword,custconfirmpassword)values('{}','{}','{}','{}','{}','{}')".format(customer.getCustName(),customer.getCustEmail(),customer.getCustContact(),customer.getCustAddress(),customer.getCustPassword(),customer.getCustConfirmPassword())
            print(sqlquary)
            i=mycur.execute(sqlquary)
            if i>0:
                conn.commit()
                conn.close()
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def deleteCustomer(self,cust):
        pass

    def updateCustomer(self,cust):
        pass

    def showCustomerList(self):
        try:
            customerlist=[]
            sqlquary = "select *from customer"

            print(sqlquary)
            i = mycur.execute(sqlquary)
            if i > 0:
                data=mycur.fetchall()
                for row in data:
                    custobj=Customer(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                    customerlist.append(custobj)
                return customerlist
            else:
                return None
        except Exception as e:
            print(e)


    def searchCustomerById(self,custid):
        pass

    def searchCustomerByEmailId(self,custemail):
        pass