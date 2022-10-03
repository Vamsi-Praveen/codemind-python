s=input().split()
x=0
y=0
for i in s:
    l=[]
    for j in i:
        l.append(ord(j))
    x+=min(l)
    y+=max(l)
print(y-x)