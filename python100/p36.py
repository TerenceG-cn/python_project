# 输出指定范围内的素数
import math

start = 1
end = 1000000000000
boolList = []


def select(booList, last, run):
    for i in range(2, int(last / run) + 1):
        booList[i * run] = False


for n in range(end + 1):
    if n % 2 != 0:
        boolList.append(True)
    else:
        boolList.append(False)

# print(boolList)
# # print(boolList.__len__())
# select(boolList,end,9)
# print(boolList)

for i in range(2, end):
    if boolList[i]:  # 对筛选后的结果进行求素数
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                boolList[i] = False
                break
        select(boolList, end, i)  # 如果为素数，那该素数的倍数必然非素数，筛选！
count = 0
for j in range(start, end + 1):
    if boolList[j]:
        print(str(j) + '\t', end=' ')
        count += 1
        if count % 10 == 0:
            print()
print()
print("count 质数:" + str(count))
# ????????????????????????????????????????????????????
