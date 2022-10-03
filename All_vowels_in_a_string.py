n=input()
vowels=['a','e','i','o','u']
for i in n:
    if i in vowels:
        vowels.remove(i)
if len(vowels)==0:
    print("True")
else:
    print("False")