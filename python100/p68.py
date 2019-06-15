# 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数


def move(array, n, m):
    array_end = array[n - 1]
    for i in range(n - 1, -1, -1):  # for i in range(0,n):
        array[i] = array[i - 1]
    array[0] = array_end
    m -= 1
    if m > 0:
        move(array, n, m)


numlist = [1, 4, 7, 4, 7, 9, 11, 1, 6, 5]

list1 = numlist[:]
move(list1, 10, 2)
print(list1)
