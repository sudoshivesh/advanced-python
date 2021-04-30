class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def get(self):
        return(self.x,self.y)
class Location(Point):
    def __init__(self,x1,y1,x2,y2):
        self.Source=Point(x1,y1)
        self.Destination=Point(x2,y2)
    def show(self):
        print("Source: ",self.Source.get())
        print("Destination: ",self.Destination.get())
    def reflection(self):
        self.Destination.x=-self.Destination.x
        print("Reflection point on X axis is: ",self.Destination.x,self.Destination.y)

L=Location(1,2,3,4)
L.show()
L.reflection()
        
        
        
