a,b=map(int, input().split())
while(b):
    if a>b:
        a=a+b;
        b=a-b;
        a=a-b;
    b=b%a;
print(a);