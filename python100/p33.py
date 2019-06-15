# 按逗号分隔列表。

l = [1, 2, 3, 4, 5]

result = ','.join(str(n) for n in l)
print(isinstance(result, str))
print(result)

print(str(a) for a in l)
