def sum_fac(n):
    Sum=[]
    for i in range(1,n):
        if n%i==0:
            Sum.append(i)
    return sum(Sum)
n=int(input())
if (sum_fac(n)>n):
    print("True")
else:
    print("False")