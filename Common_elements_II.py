n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr1=list(map(int,input().split()))
l=[]
for i in arr:
    for j in arr1:
        if i not in arr1 and i not in l:
            l.append(i)
for i in arr1:
    for j in arr:
        if i not in arr and i not in l:
            l.append(i)
print(*l)