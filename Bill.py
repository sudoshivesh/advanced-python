class Store:
    product_Code=[]
    product_Price=[]
    quantity_required=[]

    def __init__(self):
        self.quantity=int(input("How Many Product do You Have? "))
        for i in range(self.quantity):
            self.product_Code.append(int(input("Enter Code Of Product: ")))
            self.product_Price.append(int(input("Enter Price Of Product: ")))
        print()
            
    def display_Menu(self):
        print("S.No \t Code \t Price")
        for i in range(self.quantity):
            print(i+1,"\t",self.product_Code[i],"\t",self.product_Price[i])
        print()

    def quantity_Required(self):
        print("Only Enter the Quantity of Each Item : ")
        for i in range(self.quantity):
            self.quantity_required.append(int(input()))
        print()

    def bill(self):
        total=0
        for i in range(self.quantity):
            total+=self.product_Price[i]*self.quantity_required[i]
        print("*************HERE IS YOU BILL******************")
        print("S.No \t Code \t Price \t Quantity \t Subtotal")
        for i in range(self.quantity):
            print(i+1,"\t",self.product_Code[i],"\t",self.product_Price[i],"\t",self.quantity_required[i],"\t \t",self.quantity_required[i]*self.product_Price[i])
        print("************************************************ \n")
        print("Your Final Price: ",total,"\n")
        
        
        

s=Store()
s.display_Menu()
s.quantity_Required()
s.bill()
print("**********  THANKS FOR SHOPPING. WE WOULD LOVE TO SEE U AGAIN  *********")
print("**********  Mail us if you have any Feedback to [store@gmail.com]  **********")
        
            
        
            
            
        
                                
            
