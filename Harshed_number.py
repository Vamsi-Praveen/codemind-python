n=int(input())
Sum=0
temp=n
while(n>0):
    d=n%10
    Sum+=d
    n=n//10
n=temp
if n%Sum==0:
    print('True')
else:
    print('False')