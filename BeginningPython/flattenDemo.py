# 第一种生成器方法
def faltten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


def flatten2(nested):
    try:
        for sublist in nested:
            for element in sublist:
                yield element
    except TypeError:
        yield element


# 如果nested是字符串类型，他就属于序列，因此不会引发TypeError异常、


def flatten3(nested):
    try:
        # 不迭代类似于字符串的对象
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in faltten(sublist):
                yield element
    except TypeError:
        yield nested


n = [[1, 2], [3, 4], [5]]
for num in faltten(n):
    print(num)

# 第二种创建生成器的方法
# 使用()创建生成器，如果使用[]则创建列表
a = (x ** 2 for x in range(1, 5))
# 可以通过next一直产生新的数据，直到最后一个报异常，通过for遍历不会报异常
# 也可以使用a.__next__()
print(next(a))  # 输出1
print(a.__next__())  # 输出4
print(next(a))  # 输出9

# 通过for遍历生成器
for i in a:
    print(i)
