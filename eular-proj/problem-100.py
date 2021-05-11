# a-1/b-1 < a/b  ;  (a-1/b-1)^2 < a/b * a-1/b-1 < a^2/b^2     b=^2a-^2+1  b=^2a  ->  a=^2b-^2+2/2    a=^2*b/2
import math
c = pow(0.5,0.5)
#b=pow(10,12)
b=22280241075
flag=0
while flag==0:
    # end=math.floor(start+1-SQRT2/2)
    a=math.floor(c*b+1-c)
    print(a)
    if(2*a*(a-1)==b*(b-1)):
        flag+=1
        print(a,b)
    b+=1
    
# todo 




