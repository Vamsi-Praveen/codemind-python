n=int(input())
arr=list(map(int,input().strip().split()))[:n]
# print(arr)
l=[]
for i in range(0,len(arr)):
    c=0
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j] and i!=j:
            c+=1
    if c==0:
        l.append(int(arr[i]))
print(sum(l))