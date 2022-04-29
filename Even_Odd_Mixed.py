n=int(input())
c,k,f=0,0,0
while(n>0):
    d=n%10
    if d%2==0:
        c+=1
    else:
        k+=1
    n=n//10
    f+=1
if c==f:
    print("Even")
elif k==f:
    print("Odd")
else:
    print("Mixed")