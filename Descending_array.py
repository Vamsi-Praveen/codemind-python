n=int(input())
arr=list(map(int,input().split()))[:n]
if arr==sorted(arr,reverse=True):
    print("yes")
else:print("no")