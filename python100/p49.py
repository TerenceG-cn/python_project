# 使用lambda来创建匿名函数

MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
    # a = 10
    # b = 20
    # print('The largar one is %d' % MAXIMUM(a, b))
    # print('The lower one is %d' % MINIMUM(a, b))
    a = -1
    print((10 > 20) * 10 + (10 < 20) * 10)
    if 1 is True:
        print("1 is True")
    if 1 == True:
        print("1 == True")
    if False == 0:
        print("Falsee==0")
    if a == True:
        print("a==True")
    if a:
        print("a not null")
