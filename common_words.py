a=(input().lower()).split()
b=(input().lower()).split()
l=[]
for i in b:
    if i in a and i not in l:
        l.append(i)
print(*l)