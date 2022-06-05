from fractions import gcd
from functools import reduce
def find_gcd(list):
    x = reduce(gcd, list)
    return x
n=int(input())
arr=list(map(int,input().split()))[:n]
print(find_gcd(arr))