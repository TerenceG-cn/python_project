from sys import *

if __name__ == '__main__':
    def encryption(a):
        aa = []
        aa.append(a % 10)
        aa.append(a % 100 // 10)
        aa.append(a % 1000 // 100)
        aa.append(a // 1000)

        for i in range(4):
            aa[i] += 5
            aa[i] %= 10
        for i in range(2):
            aa[i], aa[3 - i] = aa[3 - i], aa[i]
        print('解密后：', end='')
        for i in range(3, -1, -1):
            stdout.write(str(aa[i]))


    def decrypt(a):
        aa = []
        aa.append(a % 10)
        aa.append(a % 100 // 10)
        aa.append(a % 1000 // 100)
        aa.append(a // 1000)

        for i in range(2):
            aa[i], aa[3 - i] = aa[3 - i], aa[i]
        for i in range(4):
            aa[i] -= 5
            if aa[i] > 0:
                aa[i] %= 10
            else:
                aa[i] += 10
        print('加密后：', end='')
        for i in range(3, -1, -1):
            stdout.write(str(aa[i]))


    encryption(1783)  # 加密后 8326
    print()
    decrypt(8326)
