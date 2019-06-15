# 题目：求1+2!+3!+...+20!的和。
s = 0
for n in range(1, 21):
    t = 1
    for i in range(1, n + 1):
        t *= i
    s += t
    print(str(n) + ':' + str(s))

print('1! + 2! + 3! + ... + 20! = %d' % s)
