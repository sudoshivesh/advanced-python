#use of Generator to show performance Improvement


import random
import time
name=['Shivesh','Ciyan','Reyansh','Bunny']
subjects=['Python','Java','C++','Ruby']

def mylist(num):
    result=[]
    for i in range(num):
        person={
            'id':i,
            'name':random.choice(name),
            'subject':random.choice(subjects)
            }
        result.append(person)
    return result

def generator(num):
    for i in range(num):
        person={
            'id':i,
            'name':random.choice(name),
            'subject':random.choice(subjects)
            }
        yield person

t1=time.clock()
my_list=mylist(1000)
t2=time.clock()
print("Time Taken By the list is :",t2-t1)

t1=time.clock()
my_generator=generator(1000)
print(next(my_generator))
t2=time.clock()
print("Time Taken by generator: ",t2-t1)



