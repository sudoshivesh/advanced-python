class parent:
    def __init__(self):
        print("Parent Class ka constructor")
    def hello(self):
        print("Parents class ka method")
class child(parent):
    def __init__(self):
        print("Child class ka constructor")
        parent.__init__(self)
    def welcome(self):
        print("Child class ka method")
c=child()
