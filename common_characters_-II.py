s1=input().lower().split()
s1="".join(s1)
s2=input().lower().split()
s2="".join(s2)
l=[]
x=[]
for i in s1:
    if i in s2 and i not in l:
        l.append(i)
for i in s2:
    if i in s1 and i not in l:
        l.append(i)
print(len(l))