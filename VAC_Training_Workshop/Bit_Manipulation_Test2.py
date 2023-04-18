# Python Program to detect
# if two integers have opposite signs.

def oppositeSigns(x,y):
	product = x*y
	return (product<0)

# driver code
x = str(input())
y = str(input())
if(oppositeSigns(x, y) == True):
    print("opposite sign")
else :
    print("same sign")


# Write a program to find a letter’s position in alphabets

# Python3 implementation of the approach

NUM = 31


# Function to calculate the position
# of characters
def positions(str):
    for i in str:
        # Performing AND operation
        # with number 31
        print((ord(i) & NUM), end=" ")


# Driver code
str = input()
positions(str)
