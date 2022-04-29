n=int(input())
num=0
sq=n*n
temp=n
while(temp>0):
    num+=1
    temp=temp//10
den=round(pow(10,num))
last = sq%den
if last==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")