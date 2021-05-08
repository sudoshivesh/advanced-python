'''Abstract Class -The class which object cant be created and can only be
inherited and an object of derived class was use to accesst the feature of
the base class'''


class Fruit:
    def taste(self):
        raise NotImplementedError()
    def rich_in(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()

class  Mango(Fruit):
    def taste(self):
        return "Sweet"
    def rich_in(self):
        return "Vitamin-A"
    def color(self):
        return "yellow"

class  Orange(Fruit):
    def taste(self):
        return "Sour"
    def rich_in(self):
        return "Vitamin-C"
    def color(self):
        return "orange"

Alphonso=Mango()
print(Alphonso.taste(),Alphonso.rich_in(),Alphonso.color())
Kinnow=Orange()
print(Kinnow.taste(),Kinnow.rich_in(),Kinnow.color())


