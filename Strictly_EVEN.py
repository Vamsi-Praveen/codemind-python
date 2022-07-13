n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if i%2!=0:
        if l[i]%2==0:
            c+=1
if c>0:
    print(False)
else:
    print(True)