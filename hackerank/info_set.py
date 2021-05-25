n = int(input("enetr ih total no. of element"))
l=[]
for i in range(n):
    l.append(int(input("enter the data")))

s=set(l)
res=0
for i in s:
    res+=i
ans= res/len(s)
print(ans)

