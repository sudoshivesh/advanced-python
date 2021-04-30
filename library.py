class Library:
    def __init__(self):
        self.title=" "
        self.author=" "
        self.price=0
    def give_data(self):
        self.title=input("Enter the title of Book: ")
        self.author=input("Enter the Author name of Book: ")
        self.price=float(input("Enter the price of Book: "))
        print()
    def display(self):
        print("Title :",self.title)
        print("Author :",self.author)
        print("Price :",self.price)
        print("\n")

mybook=[]
ch='y'
while ch=='y':
    print('''
1.Add New Book
2.Display Books
''')
    choice=int(input("Enter your chocie: "))
    print()
    
    if choice==1:
        lib=Library()
        lib.give_data()
        mybook.append(lib)
    elif choice==2:
        for i in mybook:
            i.display()

    else:
        print("Its a invalid input")

    ch=input("Enter y to continue and other key to stop: ")
print("Bye")
        
        
