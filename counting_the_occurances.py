s=input()
ch=input()
c=0
for i in range(0,len(s)):
    if s[i]==ch:
        c+=1
if c!=0:
    print(c)
else:
    print(-1)