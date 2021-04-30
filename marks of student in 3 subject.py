#name of student and marks in three subject
class Student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def enterMarks(self):
        for i in range(3):
            m=int(input("Enter the marks of %s in subject %d :"%(self.name,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name,"got",self.marks)
s1=Student("Shivesh")
s1.enterMarks()
s2=Student("Ciyan")
s2.enterMarks()
s1.display()
s2.display()
