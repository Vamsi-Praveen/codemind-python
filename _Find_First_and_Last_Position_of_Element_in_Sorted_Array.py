n=int(input())
arr=list(map(int,input().split()))[:n]
k=int(input())
for  i in range(0,len(arr)):
    if arr[i]==k:
        print(i,end=" ")
        break
else:
    print(-1,end=" ")
for i in range(len(arr)-1,-1,-1):
    if arr[i]==k:
        print(i,end=" ")
        break
else:
    print(-1)