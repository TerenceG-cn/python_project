res=1
for i in range(0,7830457):
    res*=2
    if(len(str(res))>10):
        res=res%10000000000
print(res*28433+1)