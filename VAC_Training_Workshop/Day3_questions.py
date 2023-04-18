# WAP to find factorial of 'N' with function input:5 output: 120
# def fact(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     print("Factorial is :", fact)
#
#
# n = int(input())
# fact(n)

# def fact(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     print("Factorial is :", fact)


# n = int(input())
# fact(n)

# WAP to print inverted pyramid of numbers
# rows = int(input("Enter the number of rows:"))
# n = 5
# k = 1
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(k,end= " ")
#     k+=1
#     print(" ")

# inverted pyramid
# rows = int(input("Enter the number of rows:"))
# for i in range(rows, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print("\n")

# s = 'abra ka dabra'
# s.capitalize()
# s.upper()
# s.lower()
# s = 'mIet'
# s.casefold()

# Pooja would like to withdraw X rs from an ATM. The cash machine will only accept the transaction
# if X is a multiple of 5, and Pooja's account balance has enough cash to perform the  withdrawal
# transaction (including bank charges). For each successful withdrawal the bank charges 1.5 rs.
# Calculate Pooja account balance after an attempted transaction.
# First value in input would be initial balance and it is float, second value is transaction amount.
# x = int(input())
# # =1000
#     print(x,"is withdrawal from account")
#     print("Balance")


# WAP to display * right angled triangle
# *
# **
# ***
# ****
# *****
n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*', end=" ")
    print("\n")

# half diamond pyramid 
