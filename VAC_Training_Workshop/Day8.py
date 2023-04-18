# Data Structures ----> specialized form of organizing, processing, retrieving and storing the data.
# Stack Parenthesis Problem
arr = [23, 45, 56, 67,78,456]
# Singly Linked List ----> node--> data and address of next node
class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __int__(self):
        self.headval = None
list1 = SLinkedList
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3

# WAP to find the length of the largest palindrome that can be created from list / linked list.

# Doubly Linked List ----> point to prev and next node

# WAP to reverse a linked list.


# WAP for linear search on tuples
# Input: kiran sachin 24 12 the
# key: 12
# Output: found
# Search function with parameter tuple name
# and the value to be searched

'''
def search(Tuple, n):

    for i in range(len(Tuple)):
        if Tuple[i] == n:
            return True
    return False


# Tuple which contains both string and numbers.
Tuple = (1, 2, 'sachin', 4, 'Geeks', 6)


# Driver Code
n = input()

if search(Tuple, n):
    print("Found")
else:
    print("Not Found")
'''
# Search function with parameter list name
# and the value to be searched

'''
def search(List, n):
    for i in range(len(List)):
        if List[i] == n:
            return True
    return False


# list which contains both string and numbers.
List = [1, 2, 'sachin', 4, 'Geeks', 6]

# Driver Code
n = input()

if search(List, n):
    print("Found")
else:
    print("Not Found")
'''
# WAP convert a given string list to tuple.(ignore whitespaces)
# Input: virat kohli 18
# output: ('v','i','r','a','t','1','8')

string_list1 = input().split()
tuple_result = tuple(''.join(string_list1))
print(tuple_result)