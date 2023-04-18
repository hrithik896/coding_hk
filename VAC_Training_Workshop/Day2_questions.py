# #wrap to display "Hello" if number entered by user is a multiple of 5, otherwise print "Bye"
# num=int(input())
# if num%5==0:
#     print("Hello")
# else:
#     print("bye")

# age=int(input())
# if age<18:
#     print("Sorry you are still minor")
# elif age>18 and age<21:
#     print("cong not eligible")
# else:
#     print("major and eligible")

# wrap program to shows different message depending on wat time of day it is morning,
# afternoon, evening, or night (time is given in 24 hours format)

# time = int(input())
# if time<12:
#     print("Good morning")
# elif time>12 and time<16:
#     print("Good afternoon")
# else:
#     print("good evening")

# wrap to calculate the electricity bill( accept number from user) acc to the foll criteria
# unit                  price
# first 100 unit        no charge
# next 100 unit          6 rs per unit
# after 200 unit         8rs
# fix charge if rs 40 is applicable to all
# i/p: 95 o/p: 40rs only 
# i/p: 165 o/p: 430rs only 
# i/p: 225 o/p: 840rs only   


# unit=int(input())
# if unit<=100:
#     print("your bill is rs 40")
# elif unit>100 and unit <=200:
#     print("No Charge fixed charge only:",charge)
# elif unit>100 and unit<=200:
#     print("charge1")

# wrap to calculate the sum of three numbers. if the values are equal return three times their sum.

# my_list=list(map(int,input().split()))
# a,b,c=my_list
# z=a+b+c
# if a==b and b==c and a==c:
#     print("Numbers are equal and their sum is",z*3)
# else:
#     print("Numbers are not equal and sum is",z) 


# wrap to test whether m is a factor of n.....
# m=int(input())
# n=int(input())
# if m%n==0:
#     print(f"m is a factors of n")
# else:
#     print("m is not factor of n")


# wrap to remove the last digit from the given integer number..............

# num = int(input())
# print(num//10)

# wrap to check number is positive or negative..................


# program to print odd number sequence below 'N'
# input: 50
# output:
# 1
# 3
# 5
# 7
# 9
# ...
# 49

# n=int(input())
# for i in range(1,n+1,2):
#     print(i)


# fibonacci series upto n
# input: 5
# output
# 0
# 1
# 1
# 2
# 3
# 5
# 8


# leap year or not.................

# year = int(input())
# if(year%4==0 and year%100 !=0 or year%400 ==0):
#     print("Given year is a leap year")
# else:
#     print("Not a Leap Year")

# Factorial of given 'N'
# input: 5
# output: 120

num = int(input())
fact = 1
for i in range(1, num + 1):
    fact *= i
    print(fact)
