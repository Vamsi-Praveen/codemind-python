n=int(input())
a=list(map(int,input().split()))[:n]
p,q=map(int,input().split())
c=0
for i in range(len(a)):
    if a[i]<p or a[i]>q:
        print(a[i],end=" ")
        c+=1
if c==0:
    print(-1)