# Hackerrank Problem:- Strange Advertising
# day = int(input())
# people = 5
# total = 0
# for i in range(day):
#     total = total + people // 2
#     people = (people // 2) * 3
# print(total)


# WAP to print all the possible permutations of an string
# def permute(s, answer):
#     if (len(s) == 0):
#         print(answer, end=" ")
#     return
#
# for i in range(len(s)):
# 	ch = s[i]
# 	left_substr = s[0:i]
# 	right_substr = s[i + 1:]
# 	rest = left_substr + right_substr
# 	permute(rest, answer + ch)
#
#
# # Driver Code
# answer = ""
#
# s = "ABC"
#
# print("All possible strings are : ")
# permute(s, answer)

# //
# Python program to print all permutations
# with duplicates allowed
'''
def toString(List):
    return ''.join(List)


# Function to print permutations
# of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)

            # backtrack
            a[l], a[i] = a[i], a[l]


# Driver code
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1)
'''


# WAP to create a class employee and store data name, employeeid , adress,phone of
# employee under method employee data create one more method as salary calculations
# take input no of days present and calculate the exact salary you need to give

# class Employee():
#     def __init__(self, name, employee_id, address, phone, salary):
#         self.name = name
#         self.employee_id = employee_id
#         self.address = address
#         self.phone = phone
#         self.salary = salary
#
#     def salary_cal(self, ndays):
#         self.ndays = ndays
#         print((self.salary/30)*ndays)
#
#
# emp_1 = Employee('model','3333', '10000', 'Jammu', 123)
# emp_1.salary_cal(int(input()))

# Inheritance


#

# searching and sorting
# linear search
# binary
# jump
# interpolation
# sorting
# bubble
# selection
# insertion
# merge
# quick
# heap
# shell
# radix
# count

# Time Complexity  --->
# Space Complexity --->
# while calculating the complexity they drop the constant
# # WAP to sort the string 'miet'
# strr = input()
# l = sorted(strr)
# strr1 = ''.join(l)
# print(strr1)

# a4b3c1    aaaabbbc
strrr = input()
l1 = sorted(strrr)
strr2 =''.join(l1)

#
# output = ' '
# for x in sorted(str):
#     output = output + x
# WAP to find sum of digits of elements in list
# ex = [23, 34, 45, 56]
# listt = listt(map(int(input().split())))
# total = 0
# for i in list:
#     for i in strr[i]:


# WAP to print n fibonacci terms in a list using recursion---> euler theorem
# fibonacci - 1 1 2 3 5 8 13 21 34 55 89
'''
listt = [1,1]
n = int(input())
for i in range(2,n):
    listt.append(listt[i-1]+listt[i-2])
    print(listt)
'''
# WAP to generate a list where next term #
# square addition of the even digits of the previous term
# default is list = [42]
'''
listt = [42]
n = int(input())
for j in range(1,n):
    if n%2 == 0:
        print(sum(n*n))
'''

# WAP to generate a list where every next element is
# power of place value of digits of the number
# if output generated is one then square it until it is 2 digit
[1234]

