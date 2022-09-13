n=int(input())
arr=list(map(int,input().split()))
a=[]
for i in arr:
    if i not in a:
        a.append(i)
for i in range(len(a)-1):
    print(a[i],arr.count(a[i]),end=' ')
print(a[i+1],arr.count(a[i+1]))