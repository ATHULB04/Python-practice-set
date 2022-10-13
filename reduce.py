import functools
list=[1,2,3]
print(functools.reduce(lambda x,y:x+y,list))