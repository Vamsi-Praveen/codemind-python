n=int(input())
tmp=n*n
rev=0
while(n):
    d=n%10
    rev=(rev*10)+d
    n=n//10
k=rev*rev
rev=0
while(k):
    d=k%10
    rev=(rev*10)+d
    k=k//10
if tmp==rev:
    print('True')
else:
    print('False')