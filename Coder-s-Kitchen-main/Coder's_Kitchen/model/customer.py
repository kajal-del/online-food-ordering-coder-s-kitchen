class Customer:
    def __init__(self,custid=0,custname=None,custemail=None,custcontact=None,custaddress=None,custpassword=None,custconfirmpassword=None):
        self.custid=custid
        self.custname=custname
        self.custemail=custemail
        self.custcontact=custcontact
        self.custaddress=custaddress
        self.custpassword=custpassword
        self.custconfirmpassword=custconfirmpassword

    def setCustId(self,custid):
        self.custid=custid

    def setCustName(self,custname):
        self.custname=custname

    def setCustEmail(self,custemail):
        self.custemail=custemail

    def setCustContact(self,custcontact):
        self.custcontact=custcontact

    def setCustAddress(self,custaddress):
        self.custaddress=custaddress

    def setCustPassword(self,custpassword):
        self.custpassword=custpassword

    def setCustConfirmPassword(self,custconfirmpassword):
        self.custconfirmpassword=custconfirmpassword

    def getCustId(self):
        return self.custid

    def getCustName(self):
        return self.custname
    def getCustEmail(self):
        return self.custemail

    def getCustContact(self):
        return self.custcontact

    def getCustAddress(self):
        return self.custaddress

    def getCustPassword(self):
        return self.custpassword

    def getCustConfirmPassword(self):
        return self.custconfirmpassword

    def __str__(self):
        return "customer[custid={},custname={},custemail={},custcontact={},custaddress={},custpassword={},custconfirmpassword={}]".format(self.custid,self.custname,self.custemail,self.custcontact,self.custaddress,self.custpassword,self.custconfirmpassword)
