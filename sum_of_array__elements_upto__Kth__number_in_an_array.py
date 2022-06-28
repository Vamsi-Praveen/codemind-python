n=int(input())
arr=list(map(int,input().split()))[:n]
k=int(input())
sum=0
for i in range(len(arr)):
    sum=sum+arr[i]
    if arr[i]==k:
        break
print(sum)