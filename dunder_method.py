class shiv:
        def __init__(self,name,var):
                self.var=var
                self.name=name
        def __repr__(self):
                return repr(self.var)
        def __len__(self):
                return len(self.name)
        def __cmp__(self,obj):
                return self.var-obj.var
obj=shiv("abcdef",1)
print("Value stored in object: ",repr(obj))
print("Length of name stored in object: ",len(obj))

obj1=shiv("ghijkl",10)
value=obj.__cmp__(obj1)
if value==0:
        print("Both values are equal")
elif value==-1:
        print("first value is less than second")
else:
        print("Second value is less than first")

