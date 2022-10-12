n=input().lower().split()
n="".join(n)
x=""
for i in n:
    if i not in x:
        x+=i
print(len(x))