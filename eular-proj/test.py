import copy

f1=[1,2,3]
f2=copy.deepcopy(f1)
del f1[0]
print(f1,f2)
