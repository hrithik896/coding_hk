'''
Given a dictionary of N elements with an alphabet as key and list of integers as value,
and a search value (intgers), return a list of all keys where the search
value appears in the list. Print -1 if the search value not found
'''

n = int(input())
d = {}
for i in range(n):
    key,*values = input().split()
    d[key] = list(map(int, values))
search = int(input())
result = [key for key, values in d.items() if search in values]
if result:
    print(result)
else:
    print(-1)

'''
Mr. Honey is the manager of BoltWire, an E-commerce platform that sells the following items for its customers online.

S.No.   Item Name             Item ID     Cost per Item       Tax%

----- | ---------------- | --------- | --------------- | ---------

1.          Bulb                      16521         60.00                  5

2.          UPS                      26521        5000.00              10

3.          Fan                       26522        1000.00              8

4.          Charger               26523         500.00               10

5.          Motor                   26524         2000.00             15

 

Mr. Honey wants a program to generate bill including Tax, for 'n' items per user based on the item ID and number of units provided as the input. Help Mr. Honey to complete the bill generation task.


Constraints:
Item ID and Number_units must be an integers


Example:
Input:

2

26521 2

16521 20

Output:

12260.00


Explanation:
Cost per Unit for Item ID 26521 is 5000.00 and Tax amout will be 500.00. So, cost per unit including tax 5500.00 and bill for 2 units will 11000.00.

Similarly, for second item price 1260.00.

Total bill amount will be 12260.00
'''

items = {
    16521: {'name': 'Bulb', 'cost' : 60.00, 'tax': 5},
    26521: {'name': 'UPS', 'cost' : 5000.00, 'tax': 10},
    26522: {'name': 'Fan', 'cost' : 1000.00, 'tax': 8},
    26523: {'name': 'Charger', 'cost' : 500.00, 'tax': 10},
    26524: {'name': 'Motor', 'cost' : 2000.00, 'tax': 15}
    }
n = int(input())
total_cost = 0
for i in range(n):
    item_id,units = map(int,input().split())
    item = items[item_id]
    cost = item['cost'] * units * (1 + item['tax']/100)
    total_cost += cost
print("{:.1f}".format(total_cost))

'''
Count the number of occurrence of each character from the given string and print in dictionary.


Constraints:
NA


Example:
I/p:

letter

O/p:

{'l': 1, 'e': 2, 't': 2, 'r': 1}
'''

s = input()
counts = {}
for char in s:
    if char in counts:
        counts[char] +=1
    else:
        counts[char] = 1
print(counts)

'''
 Consider the following are mirror characters:

b->d  d->b v->v o->o x->x i->i w->w

Read a String, perform its mirror imaging, return “-1” if mirror image not possible using english characters.


Constraints:
NA


Example:
Example 1:

I/p:

void

O/p:

voib

Example 2:

I/p:

word

O/p:

-1


Explanation:
Input : test_str = ‘void’

Output : voib

Explanation : d replaced by b and vice-versa as being mirror images.

Input : test_str = ‘gfg’

Output :-1

Explanation : Valid Mirror image not possible.


Public Test Cases:
#	INPUT	EXPECTED OUTPUT
1	
void
voib
2	
word
'''

mirror = {
    'b': 'd',
    'd': 'b',
    'v': 'v',
    'o': 'o',
    'x': 'x',
    'i': 'i',
    'w': 'w'
}
s = input()
mirror_s = ""
for char in s:
    if char in mirror:
        mirror_s +=mirror[char]
    else:
        print("-1")
        break
else:
    print(mirror_s)

'''
Write a program to read a dictionary from user and rotate the dictionary k times. Print the rotated dictionary .


Constraints:
I/p:

First line consists of total number(n) of key and value pairs present in dictionary

From the second line we have to give Key space value and in the new line we have to give key and value untill it reaches nth line

Last line should take how many rotations as input

O/p:

print rotated dictionary.


Example:
I/P:

4
4 67
3 90
1 45
2 345
2

O/P:
{'1': '45', '2': '345', '4': '67', '3': '90'}


Explanation:
NA


Public Test Cases:
#	INPUT	EXPECTED OUTPUT
1	
4
4 67
3 90
1 45
2 345
2
{'1': '45', '2': '345', '4': '67', '3': '90'}
mirror = {
    'b': 'd',
'''

n = int(input())
d = {}
for i in range(n):
    key, value = input().split()
    d[key] = value
k = int(input())
for i in range(k):
    last_key = list(d.keys())[-1]
    last_value = d.pop(last_key)
    d = {last_key: last_value, **d}
print(d)