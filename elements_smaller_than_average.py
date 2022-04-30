n=int(input())
arr=list(map(int,input().strip().split()))[:n]
c=0
avg=sum(arr)//len(arr)
for i in range(0,len(arr)):
    if arr[i]<=avg:
        c+=1
print(c)
