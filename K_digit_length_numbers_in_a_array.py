n,k=map(int,input().split())
arr=list(map(int,input().split()))[:n]
l=[]
c=0
for i in range(len(arr)):
    if arr[i]<0:
        arr[i]=-(arr[i])
    l.append(len(str(arr[i])))
for i in range(len(l)):
    if l[i]==k:
        c+=1
print(c)