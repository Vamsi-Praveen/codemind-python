n=int(input())
Sum=0
v=0
arr=list(map(int,input().strip().split()))[:n]
k=int(input())
for i in range(0,len(arr)):
    t=int(arr[i])
    c=0
    for j in range(1,t+1):
        if t%j==0:
            c+=1
    if c==2:
        if(arr[i]>=k):
            v+=1
print(v)
        