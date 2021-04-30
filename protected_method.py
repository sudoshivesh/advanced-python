class protected_method:
        _schoolname="XYZ public school"    #protected Class attribute

        def __init__(self,name,age):
                self._name=name      #protected instance variable
                self._age=age     #protected instance variable
                print("Name: ",self._name,"age: ",self._age)
                
pm=protected_method("Shivesh",20)
print(pm._name)
