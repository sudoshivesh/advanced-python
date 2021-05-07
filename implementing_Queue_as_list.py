class Queue:
    def __init__(self):
        self.q=[]
        self.front=None

    def enqueue(self,item):
        self.q.append(item)
        if(len(self.q)==1):
            self.front=self.rear=0
        else:
            self.rear=len(self.q)-1

    def isempty(self):
        if(self.q==[]):
            return True
        else:
            return False
    def dequeue(self):
        if(a.isempty()):
            return "underflow"
        else:
            self.ite=self.q.pop(0)

        if(len(self.q)==0):
            self.front=self.rear=None
        return self.ite
    def Display(self):
        if(a.isempty()):
            print("queue Empty \n")
        elif(len(self.q)==1):
            print(self.q[0],"<==front as well as rear")
        else:
            self.front=0
            self.rear=len(self.q)-1
            print(self.q[self.front],"<--front")
            for t in range(1,self.rear):
                print(self.q[t])
            print(self.q[self.rear],"<--rear")


a=Queue()
while True:
    print("_"*50)
    print("Queue Operations")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    print("_"*50)

    ch=int(input("Enter your choice (1-5): "))
    if(ch==1):
        val=int(input("Enter Item: "))
        a.enqueue(val)
        input("press any key to continue ")
    if(ch==2):
        returnvalue=a.dequeue()
        if(returnvalue=="underflow"):
            print("Queue is empty \n")
        else:
            print("Dequeue item= ",returnvalue)
        input("press any key to continue ")
    if(ch==3):
        a.Display()

    if(ch==4):
        print("Thanks for trying Queue Operation")
        break
    
        
