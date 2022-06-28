n=int(input())
arr=list(map(int,input().split()))[:n]
k=int(input())
for i in range(len(arr)):
     if arr[i]==k:
         print("True")
         break
else:
    print("False")