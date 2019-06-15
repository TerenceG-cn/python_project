# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def output(str, len):
    if len == 0:
        return
    print(str[len - 1], end='')
    output(str, len - 1)


s = input('Input a string:')
l = len(s)
output(s, l)
