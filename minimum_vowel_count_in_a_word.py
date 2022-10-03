a=input().lower().split()
x=set("aeiou")
v=0
for i in a:
    c=0
    v+=1
    for j in i:
        if j in x:
            c+=1
    if v==1:
        ma=c
    if c<ma:
        ma=c
print(ma)
        