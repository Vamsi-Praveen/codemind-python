def amicable(a,b):
    f1=[]
    f2=[]
    for i in range(1,a+1):
        if a%i==0:
            f1.append(i)
    for i in range(1,b+1):
        if b%i==0:
            f2.append(i)
    if sum(f1)==sum(f2):
        return "Amicable"
    else:
        return "Not Amicable"
a=int(input())
b=int(input())
print(amicable(a,b))