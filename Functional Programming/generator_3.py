def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
rev=rev_str("Shivesh")  '''you may also write for char in rev_str("Hello")'''
for char in rev:
    print(char)
