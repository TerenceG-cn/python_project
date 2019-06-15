num = str(int(input("请输入一个数字：")))
# print(len(num))
flag = 1
for i in range(int(len(num) / 2)):
    if num[i] != num[len(num) - i - 1]:
        flag = 0
        break
if flag == 1:
    print("true")
else:
    print("false")
