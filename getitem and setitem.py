class Numbers:
        def __init__(self,mylist):
                self.mylist=mylist
        def __getitem__(self,index):
                return self.mylist[index]
        def __setitem__(self,index,val):
                self.mylist[index]=val
NumList=Numbers([1,2,3,4,5,6,7,8,9])
print(NumList[5])
NumList[3]=10
print(NumList.mylist)
