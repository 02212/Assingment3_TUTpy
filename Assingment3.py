# KJ Ntsoane
# 219023456
# 18/02/2023
# Assingment 3: Python

# Problem 1

# Given the string:
s = "fullstackslp"

# Use indexing to print out the following:
# "f"

pos_f = s.find('f')
print(s[pos_f])
# "p"
pos_p = s.find('p')
print(s[pos_p])

# "stack"

pos_s = s.find('s')
pos_k = s.find('k') + 1
print(s[pos_s: pos_k])

#slp

pos_P = s.find('p') + 1
pos_S = pos_P - s.find('s') + 1
print(s[pos_S: pos_P])

# "cks"

pos_S = pos_P - s.find('s') + 2
pos_c = s.find('c')
print(s[pos_c: pos_S])

# Problem 2 - Lists

d1 = {'simple_key': 'hello'}
print(d1['simple_key'])

d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d3['k1'], ['nest_key'])


# Problem 4
#Identifying and displaying unique(same) numbers in a list

mylist = [1, 1, 1, 1, 1, 2,2,2,2,2,3,3,3,3]

uniqueVal = set(mylist)
print('The unique values are: ')
lst_vals = (list(uniqueVal))
for i in lst_vals:
    print(i)

age = 45
name = 'kyle'
print("hello my dog's name is "+name+" and he looks " +str(age)+ " years old")