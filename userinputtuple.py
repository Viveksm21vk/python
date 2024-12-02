import math
'''l=[]
n = int(input("Please enter number of elements need to be stored in tuple:"))
for i in range(n):
    l.append(int(input()))
t = tuple(l)
print(t)
print(max(t))
print(min(t))'''

s = set()
n = int(input("Please enter number of elements need to be stored in tuple:"))
for i in range(n):
    s.add(int(input()))
t = tuple(s)
print(t)
print(max(t))
print(min(t))