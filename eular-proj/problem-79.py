# 本身可以写的更简单，没有考虑更复杂的情况 有相同数字？ todo 
nums = []
for line in open("eular-proj/p079_keylog.txt"):
    nums.append(line[:-1])
result=""
for line in nums:
    n1 = line[0]
    n2 = line[1]
    n3 = line[2]
    if n1 not in result:
        result += n1
        n1_i = len(result) - 1
    else:
        n1_i = result.find(n1)

    if n2 not in result:
        result += n2
        n2_i = len(result) - 1
    else:
        n2_i = result.find(n2)
    if n1_i > n2_i:
        result = result[:n2_i] + n1 + result[n2_i:n1_i] + result[n1_i + 1:]
        n1_i, n2_i == n1_i + 1, n1_i

    if n3 not in result:
        result += n3
        n3_i = len(result) - 1
    else:
        n3_i = result.find(n3)
    if n2_i > n3_i:
        result = result[:n3_i] + n2 + result[n3_i:n2_i] + result[n2_i + 1:]
        n2_i, n3_i == n2_i + 1, n2_i
print(result)