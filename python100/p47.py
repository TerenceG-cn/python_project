def exc(a, b):
    a, b = b, a
    return (a, b)


if __name__ == '__main__':
    x = 10
    y = 20
    print('x = %d,y = %d' % (x, y))
    x, y = exc(x, y)
    print(x, y)
    print(exc(x, y))
    print('x = %d,y = %d' % (x, y))
