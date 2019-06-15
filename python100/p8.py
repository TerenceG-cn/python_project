# 9*9乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d " % (i, j, i * j), end="")
    print()

# python3 中 print(x,end="")可以实现打印不换行的效果
