n=int(input())
for i in range (0,n):
    string=input()
    s=0
    for j in string:
        if j in ('a','e','i','o','u'):
            s+=1
    if(s>2):
        print("happy")
    else:
        print("sad")            
        
   
              