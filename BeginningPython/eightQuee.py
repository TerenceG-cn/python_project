import random


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num, state):
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos


print(list(queens(4, (1, 3, 0))))


def queens2(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens2(num, state + (pos,)):
                    yield result + (pos,)  # (pos,)中的 , 必不可少，这样得到的才是元组


print('nmsl')
print(list(queens2(8)))
