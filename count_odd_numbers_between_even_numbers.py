n=int(input())
c=0
arr=list(map(int,input().strip().split()))[:n]
for i in range(0,len(arr)):
    if arr[i]%2==0:
        p1=i
        #print(i)
        break
arr.reverse()
# print(arr)
for j in range(0,len(arr)):
    if arr[j]%2==0:
        p2=j
        #print(j)
        break
arr.reverse()
#print(arr)
for k in range(p1,len(arr)-p2-1):
    if arr[k]%2!=0:
        # print(k,end=' ')
        c+=1
print(c)