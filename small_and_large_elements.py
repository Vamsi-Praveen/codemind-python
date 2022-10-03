n=input().split()
x=n[0]
y=n[(len(n)-1)]
l=[]
p=[]
for i in x:
    l.append(ord(i))
for j in y:
    p.append(ord(j))
print(chr(min(l)),chr(max(p)))