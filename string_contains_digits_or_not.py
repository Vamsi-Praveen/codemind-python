for j in range(int(input())):
    string=list(input())
    c=0
    n=len(string)
    for i in range(n):
        if(string[i]>='0' and string[i]<='9'):
            print("Yes")
            c=1
            break
    if(c==0):
        print("No")