from itertools import combinations
round=15
cdn=[n for n in range(2,round+2)]
sum=0
for blue in range(round//2+1,round+1):
    red=15-blue
    for com in combinations(cdn,red):
        result=1
        for i in cdn:
            if i in com:
                result*=(i-1)/i
            else:
                result*=1/i
        sum+=result
print(1//sum)
