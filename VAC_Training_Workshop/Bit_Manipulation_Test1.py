# # Write a program to toggle the k-th bit of given number
'''
n,k = list(map(int,input().split()))
print(n ^ (1<<(k-1)))
'''
# # Write a program to unset the rightmost set bit of a number?
'''
n = int(input())
k =(n & (n-1))
print(k)
'''
# Write a program to check if a positive integer is a power of 2 without using any branching or loop,
# If Yes pirnt Yes, Else No.
num = int(input())
if num ^ 1 == num + 1:
    print("Yes")
else:
    print("No")


# Write a program to compute parity of a number. If it is even print Even Parity
#  else print Odd Parity.

def getParity(n):
    parity = 0
    while n:
        parity = ~parity
        n = n & (n - 1)
    return parity


n = int(input())
if getParity(n) == 0:
    print("Even Parity")
else:
    print("Odd Parity")


# Write a program to read two numbers let it be A &B and count number of bits to be flipped to convert A to B.

def countSetBits(n):
    count = 0
    while n:
        count += 1
        n &= (n - 1)
    return count


def FlippedCount(a, b):
    return countSetBits(a ^ b)


a, b = list(map(int, input().split()))
print(FlippedCount(a, b))


