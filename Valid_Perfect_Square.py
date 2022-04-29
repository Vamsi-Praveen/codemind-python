import math
def is_valid(num):
    sq=int(math.pow(num,0.5))
    if sq**2==num:
        return True
    else:
        return False
n=int(input())
for i in range(n):
    num=int(input())
    print(is_valid(num))