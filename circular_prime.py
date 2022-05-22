def reverse(n):
    sum=0
    while(n!=0):
        d=n%10
        sum=(sum*10)+d
        n=n//10
    return sum
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
    else:
        return 1
n=int(input())
rev=reverse(n)
if(isprime(n) and isprime(rev)):
    print("circular prime")
elif isprime(n):
    print("prime but not a circular prime")
else:
    print("not prime")
