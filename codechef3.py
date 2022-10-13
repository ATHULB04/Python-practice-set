n=int(input())
for i in range(0,n):
    x,y=map(int,input().split())
    if x%y==0:
        print(x//y)
    else:
        print("-1")