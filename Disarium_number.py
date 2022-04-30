n=int(input())
tmp=n
c=0
sum=0
while(n>0):
    d=n%10
    n=n//10
    c=c+1
n=tmp
while(n):
    d=n%10
    sum=sum+pow(d,c)
    n=n//10
    c=c-1
if sum==tmp:
    print('True')
else:
    print('False')