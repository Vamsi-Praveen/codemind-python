n,k=map(int,input().split())
arr=list(map(int,input().split()))[:n]
l=[]
for i in range(0,len(arr)):
    if arr[i]<0:
        arr[i]=-(arr[i])
    arr[i]=str(arr[i])
    if k==len(arr[i]):
        l.append(arr[i])
print(len(l))