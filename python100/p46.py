tmp = True
while tmp:
    num = int(input('输入一个数：'))
    if num * num > 50:
        print(num)
        tmp = True
    else:
        tmp = False
        print('nmsl我不玩了！')
