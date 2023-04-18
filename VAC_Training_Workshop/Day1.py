# #print the prime num range 1 to n........
# n=int(input())
# for i in range(1,n):
#     print()
# if i(i==n)

# collegeName='miet'
# branch='CSE'
# age=21
# print(collegeName,branch,age,sep='\n')

# num=input("Enter the number\n")
# name=input("Enter the name\n")
# print(type(name))

# num=3
# print(type(num))

# ip = list(map(int.input().split(".")))
# print(ip,end=" ")

# x=list(map(int,input().split( ))) #seperates the values....... and returns list.....
# print(x)                 

# s=90
# print(type(s))

# s = [True, 3, 3.2, 'ss', 3+5j]
# print(type(s))

# s=[234,45,34,67,78]
# print(type(s))

#operators ====== + - * / // ** %
# ** power of
# // modular div

# a = int(input())
# print(a%2)

#relational operator
# print(7>0)

#assignment opertor
# a+=b

#membership operator
#in, not in

#identity operator
# is is not

# logical operator
# and or not 

# a= ( 8 and 4)
# print(a) 

# marks=int(input())
# print(marks>40 and marks<80)

# check even odd using bit manipulation 
'''
num = int(input())
if num & 1:
    print('odd')
else:
    print('even')
'''

#write a program to toggle k the bit of binary number

# write a program to count total number of unset bit in given number.....


#write a program to find the number of set and unset bits
ch=10010101
print(ch & ch-1)

#write a program to find the difference of set and unset bits in number

# variables
# datatypes
# operators

#write a program to find largest and smallest number between three number..........

#-------------------------------------sample question-----------------------------------------
'''current_wizard= input()
count=1
fights= int(input())
for i in range(fights):
    duo= input().split()
    if duo[1] is current_wizard:
        current_wizard= duo[0]
        count+=1
print(current_wizard,count,sep ='\n')'''
#---------------------------------------left_shift----------------------------------------------
'''6>>1 --0110'''

#------------write a program to take three numbers as inputs and print the largest and smallest numbers-------
'''x=input("enter 1st number")
y=input("enter 2nd number")
z=input("enter 3rd number")
list=[x,y,z]
print("largest number is",max(list))
print("smallest number is ",min(list))'''


#------------write a program to design a calculator----------------------
'''ch=int(input("select the operation:"))'''

# tuple1 = tuple(input(),sep=',')
# new_element = int(input())
# tuple_result = tuple1 + new_element
# print(tuple_result)