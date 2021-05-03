class node:
    def empty(stk):
        if (stk==[]):
            return True
        else:
            return False
    def push(stk,item):          #for insertion of item into stk
        stk.append(item)
        top=len(stk)-1            #finding index of last item
    def pop(stk):                 #for removal of item from stk
        if(node.empty(stk)):
            return "underflow"
        else:
            item=stk.pop()
            if (len(stk)==0):
                top=None
            else:
                top=len(stk)-1
            return item
    def peek(stk):                  #Display the top value 
        if (node.empty(stk)):
            return "underflow"
        else:
            top=len(stk)-1           #i.e value at the last or top index
            return stk[top]
    def display(stk):               #display the item in stk
        if (node.empty(stk)):
            print("stack empty")
        else:
            top=len(stk)
        for i in range(0,top):
            print(stk[i],end=' ')
        print("\n")
stack=[]
top=None
while True:
    print("-"*50)
    print("Stack Operation")
    print("1.Push")
    print("2.Pop")
    print("3.peek")
    print("4.Display Stack")
    print("5.exit")
    print("-"*50)
    ch=int(input("Enter Choice(1-5) :  "))
    if (ch==1):
        item=int(input("Enter the item: "))
        node.push(stack,item)
        print("Item Pushed Successfully.")
    elif(ch==2):
        item=node.pop(stack)
        if(item=="underflow"):
            print("underflow stack is empty")
        else:
            print("Popped item :",item)
    elif(ch==3):
        item=node.peek(stack)
        if(item=="underflow"):
            print("underflow stack is empty")
        else:
            print("top item is: ",item)
    elif(ch==4):
        node.display(stack)
    elif(ch==5):
        break
    else:
        print("Invalid Choice")
