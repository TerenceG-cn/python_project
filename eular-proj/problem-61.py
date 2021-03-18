import math


# 三边形数
def is_triangle(n):
    return math.sqrt(1 + 8 * n) % 2 == 1


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
    return math.sqrt(1 + 24 * n) % 6 == 5


# 六边形数
def is_hexagonal(n):
    return math.sqrt(1 + 8 * n) % 4 == 1


# 七边形数
def is_heptagonal(n):
    return math.sqrt(9 + 40 * n) % 10 == 7


# 八边形数
def is_octagonal(n):
    return math.sqrt(1 + 3 * n) % 3 == 2


figurate_numbers_dict = {'triange':[], 'square':[], 'pentagonal':[], 'hexagonal':[], 'heptagonal':[], 'octagonal':[]}
for num in range(1000, 10000):
    if is_triangle(num): figurate_numbers_dict['triange'].append(num)
    if is_square(num): figurate_numbers_dict['square'].append(num)
    if is_pentagonal(num): figurate_numbers_dict['pentagonal'].append(num)
    if is_hexagonal(num): figurate_numbers_dict['hexagonal'].append(num)
    if is_heptagonal(num): figurate_numbers_dict['heptagonal'].append(num)
    if is_octagonal(num): figurate_numbers_dict['octagonal'].append(num)

def dfs(res_seq,k,count):
    # print(res_seq,k,count)
    if count==len(res_seq): 
        if res_seq[k][0]%100==res_seq['triange'][0]//100:
            return True
        else: return False
    else:
        for i in res_seq:
            if res_seq[i][1]==0 and res_seq[k][0]%100==res_seq[i][0]//100:
                res_seq[i][1]=1
                return dfs(res_seq,i,count+1)
        return False    
        
for tri in figurate_numbers_dict['triange']:
    for squ in figurate_numbers_dict['square']:
        for pen in figurate_numbers_dict['pentagonal']:
            for hex in figurate_numbers_dict['hexagonal']:
                for hep in figurate_numbers_dict['heptagonal']:
                    for oct in figurate_numbers_dict['octagonal']:
                        res_seq={'triange':[tri,0],'square':[squ,0],'pentagonal':[pen,0],'hexagonal':[hex,0],'heptagonal':[hep,0],'octagonal':[oct,0]}
                        if dfs(res_seq,k='triange',count=1):
                            print(res_seq)



        
