#Program to implemet python closure
def make_copy(msg):
    msg="Hello Everyone"

    #Inner Function
    def print_copy():
        msg="Welcome Everyone"
        print(msg)
        
    print(msg)
    return print_copy

execute=make_copy("Hello Only One")
execute()
execute()
