n=input()
l=[]
for i in n.split():
    l.append(len(i))
print(max(l))