# 题目：将一个列表的数据复制到另一个列表中。

def copyList(a):
    b = a[:]
    return b


a = [1, 2, 3]
b = copyList(a)
c = a
print(a, b, c)
b[1] = 100
print(a, b, c)
