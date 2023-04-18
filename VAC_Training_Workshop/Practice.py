# Prime no. range from 1 to n
'''
n= int(input())
if n==1:
    print("1 is not a prime")
for i in range(2,n):
    if n%i==0:
        print(i)
    else:
        print("np")
'''
# Python3 program to display Prime numbers till N

# function to check if a given number is prime
'''
def isPrime(n):


# since 0 and 1 is not prime return false.
    if (n == 1 or n == 0):
        return False

# Run a loop from 2 to n-1
    for i in range(2, n):
    # if the number is divisible by i, then n is not a prime number.
        if (n % i == 0):
            return False

# otherwise, n is prime number.
        return True

# Driver code
N = 100;
# check for every number from 1 to N
for i in range(1, N + 1):
# check if current number is prime
    if (isPrime(i)):
        print(i, end=" ")
'''

# Bit Manipulation
'''
n,k = list(map(int,input().split()))
print(n ^ (1<<(k-1)))
'''
# palindrome ---> whose reverse = original number 101->reverse->101
'''
num = int(input())
n = num
rev = 0
while num>0:
    rem = num%10  # ---> to get last digit
    rev = rev * 10 + rem   # ---> updated value of reverse
    num = num//10    # to delete the last digit to get second last digit as last digit



if n == rev:
    print(n,'is palindrome')
else:
    print(n,'is not palindrome')
'''


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)