#Implementing mro when multilevel is there 
#From here we came to know the use of Algorithm C3

class O():pass
class A(O):pass
class B(O):pass
class C(O):pass
class X(A,B):pass
class Y(B):pass
class P(X,Y,C):pass

print(O.mro())
print(A.mro())
print(B.mro())
print(C.mro())
print(X.mro())
print(Y.mro())
print(P.mro())

