def sum(x,y):
    s=0
    for i in range(0,x):
        for j in range(1,y+1):
            s+=j
        y=s
        s=0    
    return y
n=int(input())
for i in range(0,n):
    m,n=map(int,input().split())
    print(sum(m,n))