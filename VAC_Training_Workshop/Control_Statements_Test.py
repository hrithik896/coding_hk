# 1.Print the Multiplication Table based on the user choice. Read table order  range and choice from
# the user.
# If choice is 1 then print the table from 1 to given number otherwise given number to 1 (reverse order).
#
# Input Specifications:
#
# Line 1: m (multiplication table number)
#
# Line 2: n (Range to print multiplication table)
#
# Line 3: choice (to decide whether 1 to n order or n to 1 order)
# 11
# 20
# 2
# 11 * 20 = 220
# 11 * 19 = 209
# 11 * 18 = 198
# 11 * 17 = 187
# 11 * 16 = 176
# 11 * 15 = 165
# 11 * 14 = 154
# 11 * 13 = 143
# 11 * 12 = 132
# 11 * 11 = 121
# 11 * 10 = 110
# 11 * 9 = 99
# 11 * 8 = 88
# 11 * 7 = 77
# 11 * 6 = 66
# 11 * 5 = 55
# 11 * 4 = 44
# 11 * 3 = 33
# 11 * 2 = 22
# 11 * 1 = 11
# 2
# 5
# 12
# 1
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50
# 5 * 11 = 55
# 5 * 12 = 60
# m = int(input())
# n = int(input())
# c = int(input())
# if c==1:
#     for i in range(1, n+1):
#         print(m,'*',i,'=',m*i)
# else:
#     for i in range(n,0,-1):
#         print(m, '*', i,'=', m*i)
#
#
# # Write a program to find Factorial of a given number?
# n = input()
# fact = 1
# if n < 0:
#     print("Sorry Factorial does not exist")
# elif n == 0:
#     print("Factorial is 0 is 1")
# else:
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
#
#
# # Python 3 program to find
# # factorial of given number
#
# # Function to find factorial of given number
# def factorial(n):
#     if n == 0:
#         return 1
#
#     return n * factorial(n - 1)
#
#
# # Driver Code
# num = 5;
# print("Factorial of", num, "is",
#       factorial(num))
#
# # Find the number of factors for the given number and print the 1st N factors of the given number ?


#  write a  program  to Count the number of vowels and consonants from the given String.
'''
str1 = input("Please Enter Your Own String : ")
vowels = 0
consonants = 0

for i in str1:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
            or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)
'''
# print("Total number of consonants and vowels")
# print(vcount)
# print(ccount)
string = input()
character_freq={}
for i in string:
    if i in character_freq:
        character_freq[i] = character_freq[i]+1
    else:
        character_freq = 1
result = max(character_freq, key = character_freq.get)
print(result)
