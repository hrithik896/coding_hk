# WAP to convert a list to a list of dictionary
# list1 = ['miet', 'model', 'institute', 'atul']
# list2 = [23, 24, 25, 26]
# output = [{'miet':23}, {'model': 34}, {'atul':45}, {'institute':56}]
'''list1 = input().split()
list2 = input().split()
listt = []
for i in range(len(list1)):
    listt.append({list1[i]: list2[i]})
print(listt)'''

# Hackerrank - Library_Fine
'''d1, m1, y1 = map(int, (input().split()))
d2, m2, y2 = map(int, (input().split()))
fine = 0
if y1 == y2:
    if m1 == m2:
        if d1 == d2:
            print(0)
        else:
            print(abs(d1-d2)*15)
    else:
        print(abs(m1-m2)* 500)
        fine = d2-d1
        print(fine+15,"Hackos")
else:
    print("10000 Hackos")'''

# Recursive Functions - When a function call itself. use stack data structure for implementation
# def rec_function(x,y):
#     statement1
#     statement2
#     ...
#     rec_function(23,45)

# WAP  to find factorial
'''def fact(x):
    if x == 1:
        return 1
    else:
        x = x*fact(x-1)
    return x
x = int(input())
print(fact(x))'''

# WAP to calculate prime number between 1-100 using recursion
def check_prime(n, i=2):
    if n == i:
        return True
    elif n%i == 0:
            return False
    else:
            return check_prime(n, i = i+1)
def num_loop(low, up):
    if up <= low:
        return 1
    elif low<up:
        num_loop(low + 1, up)
    else:
        if x:
            print(low)
            x = check_prime(low + 1)
num_loop = int(input())


# OOPS - CLASSES AND OBJECTS
# class miet():
#      def addition(self):
#         pass
# arr = miet()

# WAP to create a class cse and in that class create methods as name and data
'''class miet():
    def __init__(self,name,branch):
        self.name = name
        self.bramch = branch
    def branch(self):
        print(self.name)
    def name(self):
        pass
arr = miet('atul', 'cse')
arr.branch()
'''

# WAP to create a banking application where
# requirements :- take account number as input if acc no exists in database (verify with pin)
# if pin correct display option(withdraw, change_pin)
# if option withdraw is selected ask for amount , withdraw thee amount
# and display amount left in bank same for deposit
# if change pin  