def palin(i):
    temp=i
    res=0
    while i!=0:
        d=i%10
        res=(res*10)+d
        i=i//10
    if res==temp:
        return 1
    return 0
n=int(input())
arr=list(map(int,input().split()))[:n]
c=0
for i in arr:
    if palin(i):
        c+=1
print(c)