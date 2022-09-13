n=int(input())
k=1
l=list(map(int,input().split()))
for i in range(len(l)//2):
    print(l[i],l[n-k],end=" ")
    k+=1
if len(l)%2!=0:
    print(l[n//2],0)