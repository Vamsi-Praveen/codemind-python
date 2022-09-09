n=int(input())
l=list(map(int,input().split()))
c=d=0
for i in range(1,n-1):
    d+=1
    if (l[i-1]>l[i] and l[i+1]>l[i]) or  (l[i-1]<l[i] and l[i+1]<l[i]):
        c+=1
if c==d:print("yes")
else:print("no")