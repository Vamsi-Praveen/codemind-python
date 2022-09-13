n,m=map(int,input().split())
z={}
arr=set(list(map(int,input().split())))
arr1=set(list(map(int,input().split())))
z=arr.intersection(arr1)
print(len(z))