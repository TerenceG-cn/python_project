if __name__ == '__main__':
    a = 0x77
    b = a & 3  # a and 3
    c = a | 3  # a or 3
    d = a ^ 3  # 异或 0-1 / 1-0 = 1、
    print(a)
    print(b)
    print(c)
    print(d)
    print('10 >> 2 = ', 10 >> 2)
    print('10 << 2 = ', 10 << 2)
    print('----------------------------')
    # 按位取反
    a = 234
    b = ~a

    print('The a\'s 1 complement is %d' % b)
    a = ~a
    print('The a\'s 2 complement is %d' % a)
