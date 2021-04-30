class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Sex: ",self.sex)

class Publications:
    def __init__(self,no_RP,no_Art,no_books):
        self.no_RP=no_RP
        self.no_Art=no_Art
        self.no_books=no_books
    def display(self):
        print("Research paper Published: ",self.no_RP)
        print("Article Published: ",self.no_Art)
        print("Book Pulished: ",self.no_books)
        
class Faculty(Person):
    def __init__(self,name,age,sex,desg,dept,no_RP,no_Art,no_books):
        Person.__init__(self,name,age,sex)
        self.desg=desg
        self.dept=dept
        self.Pub=Publications(no_RP,no_Art,no_books)
    def display(self):
        Person.display(self)
        print("Designation: ",self.desg)
        print("Department: ",self.dept)
        self.Pub.display()

F=Faculty("Shivesh",20,"Male","HOD","AI",5,10,1)
F.display()
ch='y'
while ch=='y':
    ch=input("Press y to continue: ")
    if ch=='y':
        F.display()
    else:
        break
    
        
