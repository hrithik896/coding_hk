# strings
# art = 'miet'
# for i in art:
#     print(i)

# slicing in strings
# name_string[start,end,step]
# timecomplexity = O(1)
# print(art[-1:4])
# Methods in strings
# split--> 'miet'.split()
# strip--> remove spaces from left and right of the string eg: '    miet'.strip()
# count--> frequency of any element eg: a='mieeet' a.count('e')
# find()--> a.find('e')
# index()--> return index of particular value
# Validation Methods:-
# if a.alnum()
# replace--> replace in new string not original string
# a = 7
# b = 7
# print(id(a),id(b),sep=' ')

# WAP to print all substrings from original string
# ex-miet
# m i e t mi mie ie et miet iet
# # a = 'miet'
# a = input()
# for i in range(len(a)):
#     for j in range(i+1,len(a)+1):
#         print(a[i:j])

# WAP to print all substring where some of the vowels in substring equals 6 from original string
# strr = 'abcdefghijklmnopqrstuvwxyz'
# string = input()
# vowels = 'aeiou'
# key=6
# for i in range(len(string)):
#     for j in range(i+1,len(string)+1):
#         total = 0
#         for a in (string[i:j]):
#             if a in vowels:
#                 value = string.index(a)
#                 total+=value+1
#         if total==key:
#             print(string[i:j])

# WAP for following requirement
# input: a4b3c2
# output: aaaabbbcc
# s = input(int('Enter some string where alphabet symbol contains symbol followed by digit:'))
# for i in range(len(s)):
#     if i.isaalpha():
#         pass
#     else:

# WAP to merge characters 2 strings into a single string by taking characters alternatively
# s1 = input()
# s2 = input()
# new_string = ''
# for i in range(len(s1)):
#     new_string = new_string + s1[i]+s2[i]
#       print(new_string)

# Functions --> to avoid reuse of same code of statement again and again and make program more readable
# def function_name(parameters/arguments):
# statements
# return --> return the value to calling method
# def miet(a,*b):
#     print(a,b)
#     return a+b
# function_name(parameter1,parameter2)
# print(miet(25,45,56,85,67))
# 4 types of functions based on arguments


# default argument
# def e(name='quest'):
#     print(name)
# e()

# WAP to print all combination of the numbers where addition is 26 using functions
# num = int(input("Enter the number:"))
# def combinations(x):
#     for i in range(1, x):
#         if i == 1:
#             print('1 ' *x)
#         for j in range(1, i):
#             if i + j == x:
#                 print(i, j)
#                 for a in range(x):
#                     if a+i+j == x:
#                         print(a,i,j)
# num = int (input())
# combinations(num)

# List data structure
# arr = ['atul',34,78.789,True, 4+5j]
# how to traverse
# print(len(arr))
# for i in range(len(arr)):
#     print(arr[i])
# Methods in lists
# addition:
#     append()
#     insert()
# delete:
#     pop()
#     remove()
#     clear()
#     del
