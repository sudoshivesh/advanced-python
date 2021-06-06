def decor(func):
    def inner(name):
        if name=="Shivesh":
            print("Hi",name,"How Are You?")
        else:
            func(name)
    return inner

@decor
def wish(name):
    print("Bye",name,"Its Over")


wish("Bunny")
wish("Reyansh")
wish("Shivesh")
