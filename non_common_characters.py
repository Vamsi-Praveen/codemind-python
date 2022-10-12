s1=input().lower().split()
s1="".join(s1)
s2=input().lower().split()
s2="".join(s2)
l=[]
x=[]
for i in s1:
    if i not in s2:
        l.append(i)
for i in s2:
    if i not in s1:
        l.append(i)
for i in l:
    if i not in x:
        x.append(i)
print("".join(sorted(x)))