class Account:
    def __init__(self):
        self.balance=0
        print("New Account Created")
    def deposit(self):
        amount=float(input('Enter the amount to deposit: '))
        self.balance+=amount
        print('You New balace is: ',self.balance)
    def withdraw(self):
        amount=float(input("Enter the amount to withdraw: "))
        if (amount>self.balance):
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print('New Balance is: ',self.balance)
    def enquiry(self):
        print("Balace: ",self.balance)
    
a=Account()
a.deposit()
a.withdraw()
a.enquiry()
a.miniStatement()
