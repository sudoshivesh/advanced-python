'''consider this coroutine which print out name having prefix
“Dear” in it. We will send names to coroutine using send() method.'''

# Python3 program for demonstrating 
# coroutine execution
  
def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)

corou=print_name("Dear")

corou.__next__()   #we can use next(corou) in this place

# sending inputs
corou.send("Shivesh")
corou.send("Dear Shivesh")

#If we change the case of Name i.e Shivesh Here, It wont get executed
#Also the Dear must be there if we use dear, It wont get executed

