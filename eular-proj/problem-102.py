#通过三点直接求面积
def calc_area(p1, p2, p3):
        (x1, y1), (x2, y2), (x3, y3) = p1,p2,p3
        return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)

#奔驰定理
def contain_zero(a,b,c):
    oa=a
    ob=b
    oc=c
    return oa[0]*calc_area((0,0),b,c)+ob[0]*calc_area((0,0),a,c)+oc[0]*calc_area((0,0),a,b)==0 and \
    oa[1]*calc_area((0,0),b,c)+ob[1]*calc_area((0,0),a,c)+oc[1]*calc_area((0,0),a,b)==0

count=0
for line in open("p102_triangles.txt"):
    abc=line[:-1].split(",")
    a=[float(abc[0]),float(abc[1])]
    b=[float(abc[2]),float(abc[3])]
    c=[float(abc[4]),float(abc[5])]
    print(a,b,c)
    if contain_zero(a,b,c):
        count+=1
print(count)

#写的太复杂了