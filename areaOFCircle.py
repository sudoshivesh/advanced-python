class Circle:
    PI=3.14159
    def __init__(self,radius):
        self.radius=radius
    def circum(self):
        c=2*Circle.PI*self.radius
        print("The Circumference of circle is=",c)
    def area(self):
        a=Circle.PI*self.radius*self.radius
        print("The area of Circle is=",a)
c=Circle(9)
c.circum()
c.area()
