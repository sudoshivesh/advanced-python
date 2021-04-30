#name of student and marks in three subject
class Student:
    def __init__(self):
        self.name=input("Enter Name: ")
        self.roll=input("Enter Roll Number: ")
        self.marks=[]
    def enterMarks(self):
        for i in range(3):
            m=int(input("Enter the marks of %s in subject %d :"%(self.name,i+1)))
            self.marks.append(m)
    def total(self):
        m=self.marks
        return m[0]+m[1]+m[2]
        
    def display(self):
        print("STUDENT DETAIL ")
        print("Roll Number: ",self.roll)
        print("Name Of Student: ",self.name)
        print("Total Marks: ",self.total())
s=Student()
s.enterMarks()
s.total()
s.display()

