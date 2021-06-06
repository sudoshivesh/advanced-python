#A simple generator function
def my_gen():
    n=1
    print("This is printed first")
    yield n

    n+=1
    print("This is printed second")
    yield n

    n+=1
    print("This is printed last")
    yield n

#Iterating Generator using for loop
for item in my_gen():
    print(item)
