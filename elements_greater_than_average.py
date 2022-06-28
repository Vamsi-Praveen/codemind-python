n=int(input())
arr=list(map(int,input().split()))[:n]
avg=sum(arr)//len(arr)
c=0
for i in range(len(arr)):
    if arr[i]>=avg:
        c+=1
print(c)