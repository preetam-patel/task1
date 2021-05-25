a= list(map(int,input().split()))
b= list(map(int,input().split()))
c=[]
c.append(a)
c.append(b)
from itertools import product
x=(list(product(*c)))
for i in x:
    print(i,end=" ")

