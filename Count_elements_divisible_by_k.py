n,k=map(int,input().split())
c=0
arr=list(map(int,input().strip().split()))[:n]
for i in range(0,len(arr)):
    if arr[i]%k==0:
        c+=1
print(c)