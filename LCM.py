def gcd(n,m):
    if m==0:
        return n
    else:
        return gcd(m,n%m)
        
n,m=map(int, input().split())
g=gcd(n,m)
lcm=(n*m)/g
print(int(lcm))