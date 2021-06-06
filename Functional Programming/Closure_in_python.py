'''CLOSURE IN PYTHON'''

def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  #here Nested function is being returned

# We execute the function
# Output: Hello
x=print_msg("Hello")
x()

#NOTE: when we delete the print_msg using del still x() will work

'''
del print_msg    
x()                #This will even work
print_msg("Hey")   #This will not work

'''

'''Closures can avoid the use of global values
and provides some form of data hiding.
It can also provide an object oriented solution to the problem.
When there are few methods (one method in most cases)
to be implemented in a class, closures can provide an
alternate and more elegant solution'''
