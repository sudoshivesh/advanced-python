import datetime
class Person:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    def check(self):
        today=datetime.date.today()
        age=today.year-self.dob.year
        if age>=18:
            print(self.name,"you are eligible to vote")
        else:
            print("you are not eligible to vote")
P=Person("Shivesh",datetime.date(2010,6,18))
P.check()
