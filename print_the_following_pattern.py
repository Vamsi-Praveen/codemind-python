n=int(input())
for i in range(n):
    for j in range(n):
        if i==j or (n-i-1==j):print("x",end='')
        else:print('0',end='')
    print()