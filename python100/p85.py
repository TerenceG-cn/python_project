num = int(input('输入一个数：\n'))

flag = True
nineCount = 1
plusN = 9
sum = 9

while flag:
    if sum % num == 0:
        flag = False
    else:
        plusN *= 10
        sum += plusN
        nineCount += 1
print('%d 个 9 可以被 %d 整除 : %d' % (nineCount, num, sum))
r = sum / num
print('%d / %d = %d' % (sum, num, r))
