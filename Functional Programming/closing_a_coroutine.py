'''                      CLOSING A COROUTINE

to close coroutine close() method is used. When coroutine is closed
it generates GeneratorExit exception which can be catched in usual way.
After closing coroutine,if we try to send values,
it will raise StopIteration exception


consider this coroutine which print out name having prefix
“Dear” in it. We will send names to coroutine using send() method.'''

# Python3 program for demonstrating 
# coroutine execution
  
def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing Corotuine!!")

corou=print_name("Dear")

corou.__next__()   #we can use next(corou) in this place

# sending inputs
corou.send("Shivesh")
corou.send("Dear Shivesh")
corou.close()

corou.send("Shivam")   #If we send value after close(), it will raise StopIteration Exception
corou.send("Dear Shivam")   ##If we send value after close(), it will raise StopIteration Exception

#If we change the case of Name i.e Shivesh Here, It wont get executed
#Also the Dear must be there if we use dear, It wont get executed



