n=input().lower()
c=0
vowel=set("aeiou")
for i in n.split():
    i=list(i)
    x=len(i)-1
    if i[0] in vowel and i[x] not in vowel:
        c+=1
print(c)