#Stacks  and Queues
'''STACKS= Follows LIFO/FILO
A linear data structure in which elements are inserted and deleted form the top.The element at the last will be removed first. Insertion= PUSH;  Deletion= POP. {time complexity=O(1)
Applications:
1)temporary storage structure for recursive operations.
2)evaluation of arithmetic expressions in various languages.
3)checking syntax of expressions.
4) string reversal
5)operating system functionss
6)undo redo functions in a editor
OPERATIONS IN STACKS
Push ()
pop()
top()
isEmpty()
Size()
QUEUES= LILO/FIFO'''

'''stack=[23,34]
stack.append(45)
print(stack)
stack.pop()
print(stack)'''
#-------------------------------------------------------
'''def paranthesis(strr):
    stack=[]
    listt1=['[','(','{']
    listt2=[']',')','}']
    for i in strr:
        if i in listt1:
            stack.append(i)
            #index=listt1.index(i)
        elif i in listt2:
            if len(stack)==0:
                print("unbalanced paranthesis")
                return
            elif listt1[listt2.index(i)]==stack[-1]:
                stack.pop()
                continue
            else:
                print('balanced paranthesis')
                return
    if len(stack)==0:
        print("balanced #--------------------binary search------------------------
#divide and conquer algorithm
#binary search= 0+len(arr)-1//2; mid=middle index of the array.
l=[2,3,4,5,6,7]  #ascending array
key=6
low=0
high=len(l)
mid=low+high//2
if l[mid]==key:
    print("we have found our number")
elif l[mid]<key:
    l=mid+1
elif key<mid:
    high=mid-1
#again repeat all these steps until the length of array becomes one.
#time complexity= ''k=log2(n)'''
'''listt=list(map(int,input().split()))
listt.sort()   #it will sort the array into ascending order.
low=0
key=int(input())
high=len(listt)-1
while low<=high:
    mid=low+high//2
    if listt[mid]==key:
        print("element found at index: ",mid)
        break
    elif key>listt[mid]:
        low=mid+1
    elif key<listt[mid]:paranthesis")
        return
    else:
        print("unbalanced paranthesis")
        return
s=input()
paranthesis(s)'''

'''x=int(input())
y=int(input())
if(x^y <0):
    print("opposite sign")
else:
    print("same sign")'''

#------len function in python working----------
'''listt=[34,45,56]
count=0
for i in listt:
    count+=1
print(count)'''
#------queues--------------
'''from collections import deque
queue=deque()
queue.appendleft(34)
queue.appendleft()'''

#program to reverse a string without using inbuilt python functionalities

#-----------------------trees---------------------
'''types of traversals in binary trees
1)preorder= left subtree to right sub tree
2)postorder= left subtree-->right subtree-->go to the root(siblings)
3)inorder= left subtree-->visit the root-->right subtree'''
#--write a program to implement all possible combinations of a strings where it should follow
#password syntaxing;minimum=6 and one uppercase and one upper lowercase one special case and one number
#-------------------------------------------input=take a input........................................
#-------------
'''ch=int(input())
if ch & (ch-1)==0:
    print("power of two")
else:
    print("not a power")'''


#---------
'''listt=list(map(int,(input().split())))
y=listt
print(sum(y))'''

#--------------
'''listt=list(map(int,(input().split())))
sum=0
for i in listt:
    sum=sum+i
print(sum)'''

val=input().split()
key=[]
dict={}
for i in val:
    key+=[i[0]]
for i in range(len(val)):
    print(key[i],":",[val[i]])



# Circularly linked list

# Python3 program to check for
# balanced brackets.

# function to check if
# brackets are balanced

'''

def areBracketsBalanced(expr):
	stack = []

	# Traversing the Expression
	for char in expr:
		if char in ["(", "{", "["]:

			# Push the element in the stack
			stack.append(char)
		else:

			# IF current character is not opening
			# bracket, then it must be closing.
			# So stack cannot be empty at this point.
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False

	# Check Empty Stack
	if stack:
		return False
	return True


# Driver Code
if __name__ == "__main__":
	expr = "{()}[]"

	# Function call
	if areBracketsBalanced(expr):
		print("Balanced")
	else:
		print("Not Balanced")
'''

# Balanced paranthesis problem
# Input format ---> the first line contains a single letter n, the no of string.
# Each of he enxt n lines contains a ......................
# Python3 program to check for
# balanced brackets.

# function to check if
# brackets are balanced


# def areBracketsBalanced(expr):
# 	stack = []
#
# # Traversing the Expression
# for char in expr:
# 	if char in ["(", "{", "["]:
#
# # Push the element in the stack
# 	stack.append(char)
# 	else:
#
# # IF current character is not opening
# # bracket, then it must be closing.
# # So stack cannot be empty at this point.
# 		if not stack:
# 				return False
# 			current_char = stack.pop()
# 			if current_char == '(':
# 				if char != ")":
# 					return False
# 			if current_char == '{':
# 				if char != "}":
# 					return False
# 			if current_char == '[':
# 				if char != "]":
# 					return False
#
# 	# Check Empty Stack
#     if stack:
# 	    return False
# 	return True
#
#
# # Driver Code
# if __name__ == "__main__":
# 	expr = "{()}[]"
#
# 	# Function call
# 	if areBracketsBalanced(expr):
# 		print("Balanced")
# 	else:
# 		print("Not Balanced")
#
#
#
# # Operation on stacks
# # Push()
# # Pop()
# # Top() or Peek()
# #
#
#
# # Stack Data Structure
# # Implementation of stack using list data structure
# '''
# lifo ---> last in first out
# filo ---> first in last out
# only we can add or delete element from top
# underflow ---> deleting a element when your stack is empty
# overflow ---> add a element when your stack is full
# for list ---> we append in case of push
# '''
# stack = [23, 34]
# stack.append(45)
# stack.pop()
# stack[-1]
#
# # how we will create a dynamic list using c
# # implement stack using deque
# # collection --> module of python --->import deque
#
# from queue import LifoQueue
#
# stack = deque()  # here stack is object of class in module deque
# stack.append(23)
# stack.append(89)
# print(stack)
# stack.pop()
# stack
#
#
# class list:
# 	def display(self, ):
# 		print('methods calling')
#
#
# obj = list()
# obj.display(34)
'''
def parenthesis():
	stack=[]
	listt1 = ['[','(','{']
	listt2 = [']',')','}']
	for i in strr:
		if i in listt1:
			stack.append(i)
			# index = listt1.index(i)
		elif i in listt2:
			if len(stack) ==0:
				print('unbalanced parenthesis')
				return
			elif listt1[listt2.index(i)]==stack[-1]:
				stack.pop()
				continue
			else:
				print('unbalanced parenthesis')
				return
	if len(stack)==0:
		print('Balancwd')
		return
	else:
		print('Unbalanced Parenthesis')
		return
s = input()
parenthesis(s)
'''
# --------------------------------------------------------------------------------------------------#

# queue --->
# fifo ---> first in first  out
# lilo ---> last in last out
