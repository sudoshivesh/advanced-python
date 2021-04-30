#program todemonstrtare built in method
class ABC():
    '''this is the documentation'''
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("var1=",self.var1)
        print("var2=",self.var2)
obj=ABC(10,20)
obj.display()
print("obj.__dict__",obj.__dict__)
print("obj.__doc__",obj.__doc__)
print("class.__name__",ABC.__name__)
print("obj.__module__",obj.__module__)
print("class.__bases__",ABC.__bases__)

