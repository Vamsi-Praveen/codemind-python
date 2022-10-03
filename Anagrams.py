s=input().lower()
s1=input().lower()
if sorted(set(s))==sorted(set(s1)) and len(s)==len(s1):
    print("True")
else:
    print("False")