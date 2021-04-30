#program to use private method

class private_method:
        def __init__(self,var):
                self.__var=var
        def __display(self):    #private method
                print("From class method,var=",self.__var)
obj=private_method(10)
obj._private_method__display()
                        
