n=input().lower().split()
n="".join(n)
x=""
for i in n:
    if i not in x and n.count(i)<=1:
        x+=i
print("".join(sorted(x)))