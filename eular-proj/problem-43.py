from itertools import permutations


def sub_string_divisibility_enable(num):
    d2d3d4 = int(num[1:4])
    d3d4d5 = int(num[2:5])
    d4d5d6 = int(num[3:6])
    d5d6d7 = int(num[4:7])
    d6d7d8 = int(num[5:8])
    d7d8d9 = int(num[6:9])
    d8d9d10 = int(num[7:10])
    if (
        d2d3d4 % 2 == 0
        and d3d4d5 % 3 == 0
        and d4d5d6 % 5 == 0
        and d5d6d7 % 7 == 0
        and d6d7d8 % 11 == 0
        and d7d8d9 % 13 == 0
        and d8d9d10 % 17 == 0
    ):
        return True
    else:
        return False


permutation = []
sum=0
for seq in list(permutations("0123456789")):
    permutation.append("".join(seq))
for num in permutation:
    if sub_string_divisibility_enable(num):
        print(num)
        sum+=int(num)
print(sum)
