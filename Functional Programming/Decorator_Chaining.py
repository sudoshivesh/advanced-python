#Coding for testing  Decorator Chaining
#This is a examole of chainng of decorator

def decor1(func):
    def inner():
        x=func()
        return x*x
    return inner

def decor(func):
    def inner():
        x=func()
        return 2*x
    return inner

@decor1
@decor
def num():
    return 10
print(num())


'''The order in which we chain decorator, matters.'''
#First @decor then Decor1 Will be oprated
