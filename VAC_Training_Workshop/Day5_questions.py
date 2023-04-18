# WAP to print the count the even and odd digits in a given number.
# input : 45351 even_count=1 odd_count=4
"""n = int(input())
count = 0
for i in range(1,n+1):
    if n%2==0:
        print('even_count', count(i))
    # else:
    #     print('odd_count', count(i+1))
"""


# Interview Question ---> Which option is correct
'''import copy
list1 = [2, 5, [8, 0], 7]
list2 = [3, 9, 1]
list3 = copy.copy(list1)
list4 = copy.deepcopy(list2)
list1[2][0] = 777
list2[2] = 888
print("List 3 elements")
for i in range(0,len(list3)):
    print(list3[i],end=" ")
print("\t")

print("List 4 elements")
for i in range(0,len(list4)):
    print(list4[i],end = " ")
'''

# Given a list the task is to write a python program to find the index containing string.
# Input = Navya, 98, Hema, Siroj, Tarun, 78, 90, Ramya
# Output = 0 2 3 4 7
''' listt = ['Navya', 98, 'Hema', 'Siroj', 'Tarun', 78, 90, 'Ramya']
for i in range(len(listt)):
    if str(listt[i]).isalpha():
        print(i,"",end = "")
'''

#   append() ---> add to the last
# Given two lists, the task is to write a python program to remove all the common elements from the two lists.
# input: a = [1, 2, 3, 4, 5]   b = [4, 5, 6, 7, 8]
# output: list1 = [1,2,3]  list2 = [6, 7, 8]
''' 
a = input().split()
b = input().split()
list1 = []
list2 = []
for i in a:
        if i not in b:
            list1.append(i)
for j in b:
        if j not in a:
            list2.append(j)
print(list1)
print(list2)
'''

# Telemarketer phone number problem
# phone_number = int(input())
'''first_digit = int(input())
second_digit = int(input())
third_digit = int(input())
fourth_digit = int(input())
for i in range(1):
    if first_digit == 8 or first_digit == 9:
        if second_digit == third_digit:
            if fourth_digit == 7 or fourth_digit == 8:
                print("Phone Belongs to telemarketer please ignore")
    else:
        print("Please Answer")
'''
'''
a,b,c,d = map(int,input().split())
i = 0
if list[i]==8 or list[i]==9:
    if list[i+1]==list[i+2]:
        if list[i+3]==7 or list[i+3]==8:
            print("Take Call")
else:
    print("Please Ignore")
'''

# Love Letter Problem

'''
def encode(str,shift,n):
    str02 = ' '
    for i in str:
        if ' ' == i:
            str02+=' '
        elif ord(i)+shift>122:
            str02+=chr(ord(i) + shift)
        else:
            str02+=chr(ord(i)+shift)
    return str02

n = int(input())
shift = int(input())
str01 = input().lower()

print(encode(str01,shift,n))
'''

# Program to reverse a range in a list:
# range = (3:9)
# input: lst = [6,3,1,8,9,2,10,12,7,4,11]
# output: lst = [6,3,1,7,12,10,2,9,8,4,11]

# Python3 code to demonstrate working of
# Reversing a range
# Using reverse() + loop

# initializing list
test_list = [6, 3, 1, 8, 9, 2, 10, 12, 7, 4, 11]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
strt, end = 3, 9

# reversing list and assigning the range
temp = test_list[strt:end]
temp.reverse()
for idx in range(strt, end):
    test_list[idx] = temp[idx - strt]

# printing result
print("Range reversed range list : " + str(test_list))

# Given list of tuples, WAP to remove all tuples with all None Values.
# Input: [(None,None),(None,None),(3,4),(12,3),(None, )]
# Output: [(3,4),(12,3)]

# Python3 code to demonstrate working of
# Remove None Tuples from List
# Using all() + list comprehension

# initializing list
test_list = [(None,None),(None,None),(3,4),(12,3),(None, )]

# printing original list
print("The original list is : " + str(test_list))

# negating result for discarding all None Tuples
res = [sub for sub in test_list if not all(ele == None for ele in sub)]

# printing result
print("Removed None Tuples : " + str(res))
