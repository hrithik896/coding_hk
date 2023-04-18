# Migratory Birds - hackerrank
# n = int(input('size of array'))
# listt = [45, 56, 67, 78, 45, 56,56,56, 45, 45, 23]
# listtt = []
# listt = input().split()
# maxx = 0
# for i in listt:
#     if listt.count(i) >= maxx:
#         maxx = listt.count(i)
#         element = i
#         # if listt.count(i) == maxx:
#         #     for i in listtt:
#
#         if i not in listt:
#             listt.append(i)
#             if listt.count(i) == maxx:
#                 for i in listtt:
#                     if listt.count(i) == maxx:
#                         pass
#         else:
#             listtt.remove(i)
# print('element are', *listtt, 'frequency is ', maxx)


# WAP to print the element with highest frequency in given list
# listt = [45, 56, 67, 78, 45, 56, 45, 45, 23]
# listt = input().split()
# maxx = 0
# for i in listt:
#     if listt.count(i) > maxx:
#         maxx = listt.count(i)
#         element = i
# print(element, 'frequency is ', maxx)
#  Tuples Data Structure - we are using tuples to preserve the data
# Using paranthesis we can create a tuple
# arr = (23,34,45,56,True,'miet')
# methods
# count()
# clear()
# del
# index()
# sort()

# WAP to sort all the elements of list based on the function you are passing in sort method
# def elements_greater():
#     pass
# listt = [29,34,33,45]
# # based on the digits sum of the elements
# listt.sort(elements_greater)
# # output = []
# listt.sort()
# output = [29,33,34,45]
#
# t = 23,34,45,56,68
# a,b,c,*d = t
# print(t[::3])
#
# # list comprehesion
# listt = [23, 34, 34, 45]
# listtt = list(i for i in listt if i%2==0)
# print(listtt)
# output

# brian anna problem - hackerrank
# n,k=list(map(int,input().split()))
# arr=list(map(int,input().split()))
# amount=int(input())
# arr.pop(k)
# amount_anna=sum(arr)/2
# if amount_anna==amount:
#     print("bon appetit")
# else:
#     print(abs(amount-amount_anna))
#
# # Sets data structure - duplicates are not allowed,no indexing because it follows hashing
# # sett = {} --> empty dictionary
#
#
# # dictionary data structure
# # WAP to create a dynamic dictionary where you need to take 5 students
# # roll no as input and store their name ,branch,sem, as the value.
# dictt = {}
# rollno = int(input())
# for i in range(rollno):
#     roll_num = int(input())
#     name,branch,semester = input().split()
#     dictt[roll_num] = [name, branch, semester]
# print(dictt)
#
# # ---------------------------------tuples data structures------------------------
# '''tup=(23,23,True,"class")'''
#
# # write a program to sort all the elements of the list based on the function you are passing in sort method
# '''def elements():
#     pass
# listt=[23,23,24,22]
# print(listt.sort(elements))'''
# # tuples are used as a permanent storage as it is secure and cannot be modified.------
# # tuple packing-----------------------------
# '''t=23,34,3,4,45,45,34,2,1,2,456,6
# print(t)
# a,b,c,d,*e=t
# print(a,b,c,d,*e)
# print(t[::3])'''
# # --------------------------------------
# '''listt=[23,34,34,45]
# listtt=list(i for i in listt if i%2==0 )
# print(listtt)'''
#
# # sets---------------------------------------
# # duplicates not allowed,no indexes,insertion order is not present.
# # used concept called hashing to store elements.
# # cannot be kept empty as it will be a empty dictionary. can be kept empty using constructors with parameters.set().
# # iterables=lists,tuples
# # discard() --->
# '''sett={12,12,14,56,78}
# sett1={3,12,56,77,55}
# sett.add(90)
# print(sett)
# re= sett.pop()
# print(re)
# x=sett.union(sett1)
# print(x)'''
