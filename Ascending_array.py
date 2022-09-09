n=int(input())
arr=list(map(int,input().split()))[:n]
c=d=0
for i in range(1,len(arr)-1):
    c+=1
    if arr[i-1]<arr[i] and arr[i+1]>arr[i]:
        d+=1
if c==d:print("yes")
else:print("no")