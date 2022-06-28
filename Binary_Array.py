n=int(input())
arr=list(map(int,input().split()))[:n]
c=0
for i in range(len(arr)):
    if arr[i]==0 or arr[i]==1:
        c+=1
if c==len(arr):
    print("True")
else:
    print("False")