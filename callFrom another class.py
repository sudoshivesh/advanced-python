#calling a class method from another class method
class general:
        def __init__(self,var):
                self.var=var
        def display(self):
                print("Var =",self.var)
        def add_2(self):
                self.var+=2
                self.display()
obj=general(10)
obj.add_2()
