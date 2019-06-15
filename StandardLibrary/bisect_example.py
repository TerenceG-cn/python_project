import bisect

# 类似插入排序的有序插入算法
# 随机数字列表

values = [14, 85, 77, 26, 50, 45, 67, 81, 14, 36, 96, 53, 109, 69, 7, 3, 46, 44]
print('New Pos Contents')
print('--- --- --------')
l = []
for i in values:
    position = bisect.bisect(l, i)
    bisect.insort(l, i)
    print('{:3} {:3}'.format(i, position), l)
