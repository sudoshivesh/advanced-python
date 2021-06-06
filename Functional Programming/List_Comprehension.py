#List Comprehension
'''Sorting Even Number from list using for loop and list comprehension'''
input_list=[1,2,3,4,5,6,7,8,9,10]
even_list=[]
for i in input_list:
    if i%2==0:
        even_list.append(i)
print("The list of Even Numbers are: ",even_list)


'''Now We Will Do Same With the help of List Comprehension'''

input_list1=[1,2,3,4,5,6,7,8,9,10]
even_list1=[i for i in input_list1 if i%2==0]
print("The List of Even Numbers Are: ",even_list1)
