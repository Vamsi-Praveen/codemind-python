s=input()
l=[]
res=[]
vowel=set("aeiouAEIOU")
for i in range(0,len(s)):
    if s[i] in vowel:
        l.append(s[i])
for i in l:
    if i not in res:
        res.append(i)
print(*res)