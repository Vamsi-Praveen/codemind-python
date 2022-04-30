n=int(input())
arr=list(map(int,input().split()))
num=0
arr.reverse()
for j in range(len(arr)):
    if arr[j]%2!=0:
        num=arr[j]
        break
print(num)