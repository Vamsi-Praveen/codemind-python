s=input()
vowels=set("aeiouAEIOU")
v=c=d=sp=0
for i in range(0,len(s)):
    if s[i] in vowels:
        v+=1
    elif s[i]==" ":
        sp+=1
    elif s[i].isdigit():
        d+=1
    else:
        c+=1
    
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",sp)