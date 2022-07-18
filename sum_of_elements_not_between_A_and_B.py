n=int(input())
a=list(map(int,input().split()))[:n]
p,q=map(int,input().split())
s=0
for i in range(len(a)):
    if a[i]<p or a[i]>q:
        s+=a[i]
print(s)