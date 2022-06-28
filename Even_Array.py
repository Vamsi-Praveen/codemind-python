n=int(input())
arr=list(map(int,input().split()))[:n]
c=0
for i in range(len(arr)):
    if arr[i]%2==0:
        c+=1
if c==len(arr):
    print("True")
else:
    print("False")