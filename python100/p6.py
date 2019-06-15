# 题目：斐波那契数列。
def fib1(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


print(fib1(11))
print(fib2(11))
