class MyClass:
        def my_method(self,obj):
                print('in my_method method of MyClass')
                print("Name",obj.name)
                print("Age",obj.age)
                
class Person:
        def __init__(self,name,age):
                print('init called')
                self.name=name
                self.age=age
        def display(self):
                print('in display')
                print("Name",self.name)
                print("Age",self.age)
                obj=MyClass()
                obj.my_method(self)
person=Person("Shivesh",20)
person.display()
                
