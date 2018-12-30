#qsn 5 submitted by NAIRITA MITRA

class Customers:
    Bank=[]
    customers=int(input("enter no of customers(max 20) in the bank"))
    for x in range(customers):
        account_no=int(input("enter the account no of the customers in the bank"))
        Bank.append(account_no)
        name=input("enter the names of the customers in the bank")
        Bank.append(name)
        balance=int(input("enter the balance of the customer"))
        Bank.append(balance)
        account=(input("enter the account of the customer"))
        Bank.append(account)
        def Account(self,balance):
            if balance<100:
                print("the account no : {} the name of customer: {} the balance of customer: {}".format(self.account_no,self.name,balance))
            else:
                print("the balance of customer is greater than 100")
C=Customers()
C.Account(balance=68)
