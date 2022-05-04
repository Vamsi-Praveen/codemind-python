n=int(input())
c=0
arr=list(map(int,input().split()))
for i in range(1,len(arr)-1):
    if arr[i]%2==0:
        if arr[i-1]%2!=0 and arr[i+1]%2!=0:
            c+=1
print(c)