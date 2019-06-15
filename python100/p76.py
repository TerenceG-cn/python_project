if __name__ == '__main__':
    while True:
        n = int(input('input a number:'))
        sum = 0
        while n > 0:
            sum += 1 / n
            n -= 2
        print(sum)
