def is_palin(p):
    temp=p
    rev=0
    while(p>0):
        d=p%10
        rev=(rev*10)+d
        p=p//10
    p=temp
    if rev==p:
        return True
    else:
        return False
n=int(input())
for i in range(n):
    p=int(input())
    print(is_palin(p))
    