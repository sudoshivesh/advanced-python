class Student:
        _schoolName = 'XYZ School' # protected class attribute

        def __init__(self, name, age):
                self._name=name  # protected instance attribute
                self._age=age # protected instance attribute
                print("Name=",self._name,"Age=",self._age)
S=Student("Shivesh",20)
print(S._name)
