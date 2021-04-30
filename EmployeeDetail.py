#Program to keep track of number of employees in an organisation and
#also store their name designation and salary details

class Employee:
    empCount=0
    def __init__(self,name,desg,salary):
        self.empCount=0
        self.name=name
        self.desg=desg
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("There are %d employee"%Employee.empCount)
    def displayDetail(self):
        print("Name:",self.name,  "\t Designation:",self.desg, "\t Salary:",self.salary)

e1=Employee("Shivesh","Manager",50000)
e2=Employee("Reyansh","TeamLeader",40000)
e3=Employee("Bunny","Programmer",30000)
e4=Employee("Ciyan","Office Assistant",20000)
e4.displayCount()
print("Details of Employees are: ")
e2.displayDetail()
