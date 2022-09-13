def isprime(n):
    if n==1 or n==0:
        return 0
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
l=list(map(int,input().split()))
Sum=0
c=0
for i in l:
    if isprime(i):
        Sum+=i
        c+=1
print("{:.2f}".format(Sum/c))