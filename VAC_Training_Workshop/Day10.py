# ------------Graphs--------------------
# A data structure that consists of a set of nodes and set of edges that relate the nodes to each other. Set of edges describe the relationship between the nodes.
# graph= G(V,E)
# V(G)=finite,non empty set of vertices
# E(G)=set of edges
# When edges in the graph have no direction,undirected graph, whereas if they have a direction, they are a directed graph.(order of the vertices is important in dirwcted graph.)
'''
Adjacent nodes= nodes connected by an edge.
Path= sequence of vertices that connect two nodes in a graph.
Number of edges n*(n-1)
Time complexity= 0(n**2)
Weighted Graph= each edge carries a value.
LINKED-LIST IMPLEMENTATION
An 1D array used to represent vertices
A list of edges is maintained..
OPERATIONS IN GRAPHS
Backtracking and Depth-First Search= search till the end for all possible solutions. turn the side if we find a dead end.
when reached dead end, backtrack.
Graphs are represented by a 2-D matrix.
BREADTH FIRST SEARCH= can go in any direction. Used on queues.
1)put any of the graphw vertices in the back of the queue.
2)take the front item of the queue.
DEPTH FIRST SEARCH
1)Start by putting any one of the graph's vertices on top of the stack.
2)Take the top item of the stack and add it to the visited list.
3)create a list of that vertex's adjacent nodes.Add the ones which aren't in the visited list to the top of the stack.
4)Keep repeating steps 2 and 3 until the stack is empty.
'''
# write a program to solve n queens problem and print all the permutations of a string backtracking algorithm we have discussed.
# -----------------------------------------------------------------------------------
# wap to find the sum of harmonic series where series is starting form 4 and diference is 1/3 till n terms where n is the input.
# ex--n=5
# x=1/3
# output= 4+4/3 +4/9 + 4/27 +4/81
# wap to find the absolute difference between addition of even alphabets from all combinations od strings print combinations and absolute differene values of a=1,b=2 and so on.
# ex-asp
# combinations are asp,as,p,a
# constraint=string length greater than 5 and less than 20.
'''n=int(input())
x=1/3
sum=0
for i in range(4,n-1):
    sum=sum+x**i

print(sum)'''
# ---------------------------------------------------
'''ch=input()
comb=0
for i in range(len(ch)):
    for comb in range(i+comb,len(ch)+1):
        print(ch[i:comb])'''

# BFS(Breadth First Search) Algorithm


# WAP to find sum of harmonic series where series is starting from 4 and
# harmonic difference is 1/3 till n terms where n is the input
# ex- n=5 output- 4+4/3+4/9+4/27+4/81 = value

def sum(n):
    i = 1
    s = 0.0
    for i in range(1, n + 1):
        s = s + 1 / i
    return s


# Driver Code
n = int(input())
print(round(sum(n), 6))

# WAP to find the absolute difference between addition of even alphabets and
# odd alphabets from all combinations of strings print combinations and absolute difference
# values of a=1,b=2 and so on...
# ex- asp combinations- asp,as,p,a,s,sp
# absolute difference - a+p-s = 1+16-19 = 2
# constraint- string length greater than 5 and less than 20

# alphabet = ''
# for ch in range(len(alphabet)):
#
#     str1 = input()
#     total_even = 0
#     total_odd = 0
#     for i in (0, len(str1)):
#     for j in range(i + 1, len(str1) + 1):
#     print(str1[i:j])


# Greedy Algorithm


# WAP to implement sorting of linked list
# Linked list reverse
# WAP to find the palindromic strings in a given linked list.