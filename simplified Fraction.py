class Fraction:
    def get_data(self):
        self.__num=int(input("Numenator: "))
        self.__deno=int(input("Denomenator: "))
        if self.__deno==0:
            print("ZeroDivisonEror")
            exit()
            
    def __GCD(self,a,b):
        if b==0:
            return a
        else:
            return self.__GCD(a,a%b)
        
    def __simplify(self):
        common_divisor=self.__GCD(self.__num,self.__deno)
        self.__num/=common_divisor
        self.__deno/=common_divisor

    def show_data(self):
        self.__simplify()
        print("Simplified Form=",self.__num,"/",self.__deno)
f=Fraction()
f.get_data()
f.show_data()
