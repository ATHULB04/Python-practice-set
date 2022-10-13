x=int(input())
for i in range(0,x):
    x1,x2,y1,y2=map(int,input().split())
    if(x1==y1 and x2==y2):
        print("this move is not possile")
    else:
        if x1==y1 or x2==y2:
            print("YES")
        else:
            print("NO")