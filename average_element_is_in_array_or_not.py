n=int(input())
arr=list(map(int,input().split()))[:n]
x=int(sum(arr)/len(arr))
for i in range(len(arr)):
    if arr[i]==x:
        print("True")
        break
else:
    print("False")