n=int(input())
arr=list(map(int,input().strip().split()))[:n]
c=0
for i in range(0,len(arr)):
    if arr[i]==0 or arr[i]==1:
        c+=1
if c==n:
    print("True")
else:
    print("False")
    