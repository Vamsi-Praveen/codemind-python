n=int(input())
arr=list(map(int,input().split()))
if len(arr)%2==0:
    print(*arr)
else:
    arr.append(0)
    print(*arr)