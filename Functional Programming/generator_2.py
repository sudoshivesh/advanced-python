#Implementing generator in python

def mygen():
    yield 'a'
    yield 'b'    #Yield is used in place of return to be a generator
    yield 'c'

g=mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))  
print(next(g))#Raise StopIterationError


