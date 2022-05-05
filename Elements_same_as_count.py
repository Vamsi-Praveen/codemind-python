n=int(input())
l=[]
v=0
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    c=1
    for j in range(0,len(arr)):
        if arr[i]==arr[j] and i!=j:
            c+=1
    if arr[i]==c:
        l.append(arr[i])
        v+=1
res = []
[res.append(x) for x in l if x not in res]
if v!=0:
    print(*res)
else:
    print(-1)

