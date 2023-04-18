message = 'Python Is EasY'
# print('Original string:', message)
# String Methods
# Used for alignment of a string
# 1. center(width, fill_char),
# 2. ljust(width, fill_char),
# 3. rjust(width, fill_char),
# 4. zfill(width)
# print(message.center(3, '*'))
# print(message.ljust(20, '*'))
# print(message.rjust(20, '*'))
# print(message.zfill(20))
#
# month = '1'
# print(month.zfill(2))

'''Methods to work with case of the letters'''

# lower(), upper(), title(), capitalize(), casefold(), isupper(), islower(), istitle()

# print(message.lower())
# print(message.upper())
# print(message.title())
# print(message.capitalize())
# print(message.casefold())
# print(message.swapcase())
# print(message.isupper())
# print(message.islower())
# print(message.istitle())

# Testing start and end methods
# startswith(string), endswith(string)
# print(message.startswith('Python Is'))
# print(message.endswith('sY'))

message = '_abc123'
# print(message.isalpha())
# print(message.isnumeric())
# print(message.isalnum())
# print(message.isidentifier())

message = 'Hello! welcome to python sessions!!!'
# split(string)
# print(message.split('Hello'))
# print(message.partition('o'))

data = message.split('o')
# print(data)
# res = 'RRR'.join(data)
# print(res)

'''
Write a program to read a string from the user. Find the number of 
alphabets, digits, and special symbols.
'''
# string = input()
# a_count, d_count, s_count = 0, 0, 0
#
# for character in string:
#     if character.isalpha():
#         a_count += 1
#     elif character.isnumeric():
#         d_count += 1
#     else:
#         s_count += 1
# print(f'Alphabets: {a_count}, Digits: {d_count}, Specials: {s_count}')
#
#

# given_date = input().split()        # "22nd Dec 2022" ---> ["22nd", "Dec", "2022"]
#
# months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#
# year = given_date[2]
# month = months.index(given_date[1])
# day = given_date[0][:-2]
#
# print(year, str(month).zfill(2), day.zfill(2), sep = '-')
# LIST
'''
A list is a collection of ordered, indexed, repeatable, and mutable 
elements of any type.
'''

# 1. The list was implemented using a built-in class 'list'
# 2. The list is represented using square brackets - []
# 3. All the elements in a list are stored in the order insertion
# 4. All the elements are indexed in both positive and negative
# 5. List allows duplicate elements
# 6. All the elements of a list are changeable.

# How to create list?
# 1. list_name = []
# 2. list_name = [value1, value2, ...]
# 3. list_name = list()
# 4. list_name = list(sequence)

l1 = []
l2 = [1,2,3,4,5]
l3 = list()
l4 = list(l2)

# print(type(l1))
# print(type(l2))
# print(type(l3))
# print(type(l4))


# How to access list and its elements?
# 1. Accessing entire list -------------> list_name
# 2. Accessing individual elements -----> list_name[index]
# 3. Accessing sub-list ----------------> slicing

# print(l4)
# print(l4[2])
# print(l4[1:4])

# l4[1] = 1000
# print(l4)


lst = [1,2,3]
# How to insert new elements?
# lst[3] = 4
# 1. append(e)
# 2. insert(i, e)
# 3. extend(sequence)
lst.append(40)
lst.insert(2, 20)
lst.extend([100, 200, 300])
lst.insert(10, 'Hello')
lst.extend('VMTW')
# print(lst)


# How to remove existing elements?
# 1. pop(index), 2. remove(element), 3. clear()
index = 5
lst[index-1 : index+2] = []
# print(lst)
# lst.pop(100)
# print(lst)
# lst.remove(300)
# print(lst)
# lst.clear()
# print(lst)
# lst.clear()
# print(lst)


# How update existing elements?
# list_name[index] = new_value
# We can use slicing
lst = [1,902,33,4,54,6,7,18,98,10]
# lst[3:6] = [44, 55, 66, 77, 88, 99]
# print(lst)
# lst[4:7] = []
# print(lst)




# print(lst)
# What are other features?
# count(), index(), reverse(), sort(), copy()
# print(lst.count(2))
# print(lst.index(5))
# lst.reverse()
# print(lst)
# lst.sort()
# print(lst)

# len(), max(), min(), sum(), sorted()

l1 = [1,2,3,4,5]
l2 = l1.copy()

l2[3] = 1000
l1[0] = 100

print(l1)
print(l2)
# Tuple
'''
A tuple is a collection ordered, indexed, repeatable, and immutable
elements.
'''

# 1. Tuple has implemented using a built-in class 'tuple'
# 2. Tuple is represented using round brackets or no brackets
# 3. All the elements are stored in the insertion order
# 4. All the elements has an index in both positive and negative
# 5. Tuple allows duplicate elements
# 6. Tuple does not allow inserting new values after defining it.
# 7. Tuple does not allow deleting existing elements.
# 8. Tuple does not allow to modify the existing elements.

# How to create?
# 1. tuple_name = ()
# 2. tuple_name = (value1, value2, ...)
# 3. tuple_name = value1, value2, ...
# 4. tuple_name = tuple()
# 5. tuple_name = tuple(sequence)



# How to access?
# 1. Accessing entire tuple -----------> tuple_name
# 2. Accessing individual elements ----> tuple_name[index]
# 3. Accessing sub-tuple --------------> Slicing


# How to insert?
# NOT ALLOWED


# How to Delete?
# NOT ALLOWED



# How to update?
# NOT ALLOWED



# What are additional features?
# index(e), count(e)
# len(), max(), min(), sum(), sorted()

# tpl = tuple(map(int, input().split()))
# n = int(input())
# res = []
# while n:
#     res.append(tpl)
#     n = n - 1
# res = tuple(res)
# print(res)

# Set
'''
A set is a collection of un-ordered, un-indexed, non-repeatable, and
immutable elements.
'''

# 1. Set has implemented using a built-in class 'set'
# 2. Set is represented using curly brackets - {}
# 3. All the elements are stored in random order
# 4. No element contains index
# 5. Set does not allow duplicate elements
# 6. Set allows inserting new element
# 7. Set allows deleting existing elements
# 8. Set does not allow modifying existing elements

# How to create?
# 1. set_name = {}
# 2. set_name = {value1, value2, ...}
# 3. set_name = set()
# 4. set_name = set(sequence)

# s1 = {} -------> creates a dictionary but not set
s2 = {10, 45, 89, 2, 4}
s3 = set()
s4 = set(s2)
s5 = set('rajinikanth')

# print(type(s1))
# print(type(s2))
# print(type(s3))
# print(type(s4))

# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)


# How to insert?
s = set()
# add(element), update(sequence)
# s.add(10)
# s.add(102)
# s.add(100)
# s.add(15)
# s.add(22)
# s.add(60)
#
# s.update({11, 22, 33})
# s.update('Rama')
# print(s)


# How to delete?
# pop(), remove(), discard(), clear()
# s.pop()
# print(s)
#
# s.remove('a')
# print(s)
#
# s.discard('R')
# print(s)

# How to update?
# NOT ALLOWED

# What are addition features?
# len(), max(), min(), sum(), sorted()
# union(), intersection(), difference(), symmetric_difference()
# issubset(), issuperset()

# s1 = {1,2,3,4,5}
# s2 = {10, 20, 30, 2, 3}
# s3 = {2, 100, 200, 300, 30}
#
# print(s1.union(s2, s3))
# print(s1 | s2 | s3)
#
# print(s1.intersection(s2, s3))
# print(s1 & s2 & s3)
#
# print(s1.difference(s2))
# print(s2 - s1 - s3)
#
# print(s1.symmetric_difference(s2))
# print(s2 ^ s1)
#
# print(s1.issubset(s2))
# Dictionary
'''
A dictionary is a collection elements where each element is a pair 
of KEY and respective VALUE.

Every KEY and VALUE pair is separated with a colon symbol
KEY : VALUE

---> Dictionary is represented with curly brackets - {}
---> It was implemented using a built-in class 'dict'
---> Dictionary do not have default indexing but every KEY acts as index for its VALUE.

'''

# How to create?
# 1. dict_name = {}
# 2. dict_name = {key1:value1, key2:value2, ....}
# 3. dict_name = dict()
# 4. dict_name = dict(dictionary)

student = {'rollNumber':12345, 'name': 'Ajit', 'rank' : 3, 'year' : 3}

# How to access?
# dict_name[KEY]
# print(student['name'])
# print(student)

# Access KEYs only ----> dict_name.keys()
# print(list(student.keys()))

# Access VALUEs only ----> dict_name.values()
# print(list(student.values()))

# Access both KEY and VALUE pair ----> dict_name.items()
# print(list(student.items()))


# for key, value in student.items():
#     print(f'{key} ---> {value}')
#
# for element in student:
#     print(f'{element} ---> {student[element]}')

# How to insert?
info = {}
# 1. dict_name[KEY] = VALUE
info['name'] = 'Ajit'
info['location'] = 'HYDERABAD'
info['age'] = 25
info['name'] = 'Satish'
info['age'] = 30
print(info)

# 2. update()
info.update({'height': 173, 'weight': 65, 'age': 28})
print(info)

# 3. setdefault()
info.setdefault('color', 'White')
info.setdefault('height', 175)
print(info)







# How to delete?
# pop(KEY), popitem(), clear()
#
info.pop('age')
print(info)

info.popitem()
print(info)


# How to update?
# 1. dict_name[KEY] = new_value
# 2. update()



# Additional features
# get()

print(info.get('height'))       # info['height']

# max(), min(), sorted()
print(sorted(info))
print(min(info))
print(max(info))
