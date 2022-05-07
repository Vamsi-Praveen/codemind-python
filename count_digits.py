n=int(input())
arr=list(map(int,input().split()))[:n]
for i in range(0,len(arr)):
    if arr[i]<0:
        arr[i]=-(arr[i])
    arr[i]=str(arr[i])
    print(len(arr[i]),end=' ')