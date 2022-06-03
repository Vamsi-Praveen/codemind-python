n,m=map(int,input().split())
arr=list(map(int,input().split()))[:n]
arr1=list(map(int,input().split()))[:m]
res=[]
l=[]
for i in arr:
    if i in arr1:
        res.append(i)
for i in res:
    if i not in l:
        l.append(i)
print(*l)