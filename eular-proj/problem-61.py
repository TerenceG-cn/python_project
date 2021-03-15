import math

# 三边形数
def is_triangle(n):
    if math.sqrt(1+8*n)%2==1 :
        return True
    return False    
# 四边形数
def is_square(num):
    low = 1 
    high = num
    while low < high:
        mid = (low + high) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            low = mid + 1
        else:
            high = mid - 1
    return low * low == num

# 五边形数
def is_pentagonal(n):
    # or math.sqrt(1+24*n)%6==1 广义五边形数
    if math.sqrt(1+24*n)%6==5 :
        return True
    return False 
# 六边形数
def is_hexagonal(n):
    if math.sqrt(1+8*n)%4==1 :
        return True
    return False  
# 七边形数
def is_heptagonal(n):
    if math.sqrt(9+40*n)%10==7 :
        return True
    return False  

# 八边形数
def is_octagonal(n):
    if math.sqrt(1+3*n)%3==2 :
        return True
    return False  
# for i in range(1,100):
#     n1=i*100+21
#     n2=7700+i
#     if (is_octagonal(n1) and is_triangle(n2)) or (is_octagonal(n2) and is_triangle(n1)) :
#         print(n1,n2)

# for i in range(1111,10000):
#     if is_triangle(i):
#         #print("i:",i)
#         tmp=i%100*100
#         for j in range(tmp,tmp+101):
#             if j>999 and is_square(j):
#                 #print("j:",j)
#                 tmp=j%100*100
#                 for k in range(tmp,tmp+101):
#                     if k>999 and is_pentagonal(k):
#                         tmp=k%100*100
#                         for l in range(tmp,tmp+101):
#                             if l>999 and is_hexagonal(l):
#                                 print("i j k l:",i,j,k,l)
#                                 tmp=l%100*100
#                                 for m in range(tmp,tmp+101):
#                                     if m>999 and is_heptagonal(m):
#                                         print("i j k l m:",i,j,k,l,m)
#                                         tmp=m%100*100
#                                         for n in range(tmp,tmp+101):
#                                             if is_octagonal(n):
#                                                 print(i,j,k,l,m,n)
