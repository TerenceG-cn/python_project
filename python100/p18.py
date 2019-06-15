# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
from functools import reduce

Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn += a
    a *= 10
    Sn.append(Tn)
    print(Tn)

Sn = reduce((lambda x, y: x + y), Sn)
# add=(lambda x,y:x+y)
# add(1,2)
# 3

# 描述
# reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
# 语法
# reduce() 函数语法：
# reduce(function, iterable[, initializer])
# 参数
# function -- 函数，有两个参数
# iterable -- 可迭代对象
# initializer -- 可选，初始参数
# 返回值
# 返回函数计算结果。

print('计算和：', Sn)
