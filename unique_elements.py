n=int(input())
arr=list(map(int,input().split()))[:n]
res=[]
for i in arr:
    if i not in res:
        res.append(i)
print(*res)