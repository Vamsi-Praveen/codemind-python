n=input()
c=0
d=0
s=set("aeiou")
l=[]
for i in n.split():
    c=0
    for j in i:
        if j in s:
            c+=1
    l.append(c)
x=max(l)
for i in n.split():
    c=0
    for j in i:
        if j in s:
            c+=1
    if c==x:
        d+=1
print(d)