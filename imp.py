def fun(x):
    return x**x
list=eval(input())
print([fun(x) for x in list if x%2==0])