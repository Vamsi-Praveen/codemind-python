n=int(input())
arr=list(map(int,input().split()))[:n]
for i in range(len(arr)):
    arr[i]=int(str(arr[i])[::-1])
print(*arr)