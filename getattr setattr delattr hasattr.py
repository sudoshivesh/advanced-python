#python program to demonstrate the use of getattr setattr delattr
class ABC():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("Var is: ",self.var)
obj=ABC(10)
obj.display()
print("Check if object have attribute var-----",hasattr(obj,'var'))
getattr(obj,'var')
setattr(obj,'var',50)
print("After setting values var is=",obj.var)
setattr(obj,'count',10)
print("New variable count is created and the value is=",obj.count)
delattr(obj,'var')
print("After deleting ,var is=",obj.var)
