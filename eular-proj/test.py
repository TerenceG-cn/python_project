from itertools import combinations
L = set([11,18,19,20,22,25])
result_list = sum([list(map(list, combinations(L, i))) for i in range(len(L) + 1)], [])
print('result_list =', result_list)