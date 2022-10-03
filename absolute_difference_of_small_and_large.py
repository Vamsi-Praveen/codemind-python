x=input()
l=[]
for i in x.split():
    l=[]
    i=list(i)
    for j in i:
        a=ord(j)
        l.append(a)
    print(abs(max(l)-min(l)),end=' ')