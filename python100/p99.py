# 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
# 实现步骤：
# 1.打开文件A、B并获取内容
# 2.合并排序
# 3.写入新文件C

with open('test_file.txt') as fa, open('test_file2.txt') as fb, open('result.txt', "w") as fc:
    for a in fa:
        print(a)
        b = fb.read()
        print(b)
    c = list(a + b)
    c.sort()
    d = ''
    d = d.join(c)
    fc.write(d)
