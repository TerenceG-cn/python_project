import math
import copy


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
    # return math.sqrt(1 + 24 * n) % 6 == 5 or math.sqrt(1+24*n)%6==1 广义五边形数
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


figurate_numbers_dict = {
    'triange': [],
    'square': [],
    'pentagonal': [],
    'hexagonal': [],
    'heptagonal': [],
    'octagonal': []
}
for num in range(1000, 10000):
    if is_triangle(num): figurate_numbers_dict['triange'].append(num)
    if is_square(num): figurate_numbers_dict['square'].append(num)
    if is_pentagonal(num): figurate_numbers_dict['pentagonal'].append(num)
    if is_hexagonal(num): figurate_numbers_dict['hexagonal'].append(num)
    if is_heptagonal(num): figurate_numbers_dict['heptagonal'].append(num)
    if is_octagonal(num): figurate_numbers_dict['octagonal'].append(num)


def rec_fun(tar_num, tar_polygon, fig_nums, res):
    res.append(tar_num)
    del fig_nums[tar_polygon]
    if fig_nums == {}:
        if res[0] // 100 == res[-1] % 100:
            print(res)
            print(sum(res))
        else:
            del res[-1]
    else:
        for polygon in fig_nums:
            for n in fig_nums[polygon]:
                if n // 100 == tar_num % 100:
                    new_fig_nums = copy.deepcopy(fig_nums)
                    rec_fun(n, polygon, new_fig_nums, res)
        del res[-1]


fig_nums = copy.deepcopy(figurate_numbers_dict)
for n in figurate_numbers_dict['triange']:
    rec_fun(n, 'triange', fig_nums, res=[])
    fig_nums['triange'] = figurate_numbers_dict['triange']
