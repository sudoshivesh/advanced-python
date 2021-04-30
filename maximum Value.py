class Numbers:
    values=[]
    def __init__(self):
        self.frequncy=int(input("How many Values: "))
        print("Please Enter the value to find largest value")
        for i in range(self.frequncy):
            Numbers.values.append(input())

    def find_max(self):
        max=''
        for i in Numbers.values:
            if len(i)>len(max):
                max=i
                
        print('Largest value is :',max)

n=Numbers()
print("You have Entered: ",n.values)
n.find_max()

