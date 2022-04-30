n=int(input())
arr=list(map(int,input().split()))
num=0
for j in range(len(arr)):
    if arr[j]%2==0:
        num=j
print(num)