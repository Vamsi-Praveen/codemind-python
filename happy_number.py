def ishappy(n):
    sum=rem=0
    while n>0:
        rem=n%10
        sum=sum+(rem*rem)
        n=n//10
    return sum
n=int(input())
while n!=1 and n!=4:
    n=ishappy(n)
if n==1:
    print("True")
elif n==4:
    print("False")