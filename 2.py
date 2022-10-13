from stringprep import c6_set


n=int(input())
a=1
print(a)
b=1
print(b)
for i in range(3,n+1):
    c=a+b
    print(c)
    a=b
    b=c

