#DICTIONARY COMPREHNSION
#Input a list and make it keys. Consider only even number. Values will be cubes.


'''Using For Loop'''

num=[1,2,3,4,5,6,7]
even_dict={}
for val in num:
    if val%2!=0:
        even_dict[val]=val**3
print("using for loop the dictionary is: ")
print(even_dict)


'''Using Dictionary Comprehension'''
num1=[1,2,3,4,5,6,7]
even_dict1={i:i**3 for i in num1 if i%2!=0}
print("using dictionary comprehension the dictionary is: ")
print(even_dict1)
