import math
def fac(f):
    n=1
    for i in range(1,f+1):
        n=n*i
    return n    
t=int(input())
for i in range(t):
    f=int(input())
    print(fac(f))