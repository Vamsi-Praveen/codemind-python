n=int(input())
n1=0
n2=1
c=0
if n==n1 or n==n2:
    print("True")
while n2<=n:
    temp=n2
    n2=n1+n2
    n1=temp
    if n2==n:
        c+=1
        break
if c:
    print("True")
else:
    print("False")