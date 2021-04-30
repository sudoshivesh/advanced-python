class Rectangle:
    def getdata(self):
        self.length=int(input("Enter length= "))
        self.breadth=int(input("Enter length= "))
    def area(self):
        print("AREA=",self.length*self.breadth,"sq unit")
R=Rectangle()
R.getdata()
R.area()
        
