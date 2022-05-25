s=input()
ch=input()
l=[]
res=[]
vowel=set("aeiouAEIOU")
for i in range(0,len(s)):
    if s[i] in vowel:
        if s[i]==ch:
            print(True)
            print(i)
            break
            
else:
    print(False)