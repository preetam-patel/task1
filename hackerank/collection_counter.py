n=int(input())
li= list(map(int,input().split()))
from collections  import Counter
a= Counter(li)
ans = 0
for i in range(int(input())):
	q=list(map(int,input().split()))
	value=a[q[0]]
	if value != 0:
		a[q[0]]=value-1
		ans+=q[1]
print(ans)
