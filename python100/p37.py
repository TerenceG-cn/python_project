# 题目：对10个数进行排序。

# import sys
#
# min = sys.maxsize
numList = [10, 4, 2, 6, 3, 8, 1, 5, 9, 7]


def exchange(num, i, j):
    # temp = num[i]
    # num[i] = num[j]
    # num[j] = temp
    num[i], num[j] = num[j], num[i]


def compare(a, b):
    if a >= b:
        return True
    else:
        return False


def Selction1(num):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            min = i
            if compare(num[min], num[j]):
                min = j
            exchange(num, i, min)


def Selection(num):
    for i in range(len(num)):
        min = i
        for j in range(i + 1, len(num)):
            if compare(num[min], num[j]):
                min = j
        exchange(num, i, min)


def insertion(num):
    for i in range(len(num)):
        j = i
        while j > 0 and compare(num[j - 1], num[j]):
            exchange(num, j, j - 1)
            j -= 1


def shell(num):
    N = len(num)
    h = 1
    while h < N / 3:
        h = h * 3 + 1
    while h >= 1:
        for i in range(h, N):
            j = i
            while j >= h and compare(num[j - h], num[j]):
                exchange(num, j - h, j)
                j -= h
        h = int(h / 3)


print('排序前：' + str(numList))
# Selection(numList)
# insertion(numList)
shell(numList)
print('排序后：' + str(numList))
