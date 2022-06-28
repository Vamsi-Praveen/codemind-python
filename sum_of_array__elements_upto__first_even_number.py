n=int(input())
arr=list(map(int,input().split()))[:n]
sum=0
for i in range(len(arr)):
    if arr[i]%2==0:
        break
    sum=sum+arr[i]
print(sum)