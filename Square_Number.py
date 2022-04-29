import math
def is_square(n):
    sq=math.sqrt(n)
    sq=int(sq)
    if sq*sq==n:
        return True
    return False
n=int(input())
print(is_square(n))