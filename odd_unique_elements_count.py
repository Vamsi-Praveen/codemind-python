n=int(input())
arr=list(map(int,input().strip().split()))[:n]
v=0
l=[]
for i in range(0,len(arr)):
    c=0
    for j in range(0,len(arr)):
        if arr[i]==arr[j] and i!=j:
            c+=1
    if c==0:
        if arr[i]%2!=0:
            v+=1
print(v)