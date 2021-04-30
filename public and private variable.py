#program to illustrate public and private members

class misi:
        def __init__(self,var1,var2):
                self.var1=var1
                self.__var2=var2
        def display(self):
                print("From class method,var1=",self.var1)
                print("From class method,var2=",self.__var2)
obj=misi(10,20)
obj.display()
print("From main module,var1=",obj.var1)
print("From main module,var1=",obj.__var2)


''' to acess the private variable we can use the syntax
objectname._classname__privateVariable
obj._misi__var2 '''
