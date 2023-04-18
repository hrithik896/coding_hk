'''
Write a program to read input as a tuple from user seperated with ","
and read a new element and print the tuple .
'''

tup = list(map(int,input().split(",")))
tup = tuple(tup)
new_element = list(map(int,input().split()))
new_element = tuple(new_element)
tup = tup+(new_element)
print(tup)

'''
Write a python programme to read input as a tuple from user 
seperated with "," and print the tuple repeating N times.
'''
tuple1 = (1, 2, 3, 4)
n = 3
result = ((tuple1, )*n)
print(result)
'''
Write Program to create a list of tuples with the first element as the 
number and the second element as the square of the number ?

'''
l_range = int(input())
u_range = int(input())
a = [(x, x**2) for x in range(l_range,u_range+1)]
b = list(a)
a = tuple(b)
print(a)
'''
Python Program to Find Largest Item in a Tuple ?
'''
tuple_1 = input().split(',')
result = max(tuple_1)
print(result)
'''
Program to calculate the product of a given tuple elements, multiply each and every element in a given tuple.

Input format :

Line 1 , Tuple size 

Line 2 , Tuple Elements 

Output format :

Print Tuple elements and Product of all elements


Constraints:
Tuple size > 0


Example:
NA


Explanation:
NA


Public Test Cases:
#	INPUT	EXPECTED OUTPUT
1	
6
4 3 2 2 -1 18
(4, 3, 2, 2, -1, 18)
-864

2	
5
1 2 3 4 5
(1, 2, 3, 4, 5)
120
tup = 

'''

n = int(input())
tup = list(map(int,input().split()))
tup = tuple(tup)
prod=1
for i in range(n):
    prod*=tup[i]
print(tup)
print(prod)