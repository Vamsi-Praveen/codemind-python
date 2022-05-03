n=int(input())
arr=list(map(int,input().strip().split()))[:n]
ev=[]
odd=[]
for i in range(0,len(arr)):
    if arr[i]%2==0:
        ev.append(int(arr[i]))
    elif arr[i]%2!=0:
        odd.append(int(arr[i]))
new_arr=ev+odd
print(*new_arr)