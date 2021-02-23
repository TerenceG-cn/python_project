POUND2=200
def countP1(need,count):
    for p1 in range(0,need//1+1):
        count=countP2(p1,need-1*p1,count)
    return count
    

def countP2(p1,need,count):
    for p2 in range(0,need//2+1):
        count=countP5(p1,p2,need-2*p2,count)
    return count

def countP5(p1,p2,need,count):
    for p5 in range(0,need//5+1):
        count=countP10(p1,p2,p5,need-5*p5,count)
    return count

def countP10(p1,p2,p5,need,count):
    for p10 in range(0,need//10+1):
        count=countP100(p1,p2,p5,p10,need-10*p10,count) 
    return count

def countP100(p1,p2,p5,p10,need,count):
    for p100 in range(0,need//100+1):
        if need-100*p100==0:
            print(p1,p2,p5,p10,p100)
            count+=1 
    return count

print(countP1(POUND2,0))