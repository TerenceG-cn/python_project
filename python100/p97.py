# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

# if __name__=='__main__':
#     from sys import stdout
#
#     filename = input('输入文件名：\n')
#     fp = open(filename, "w")
#     ch = input('输入字符串：\n')
#     while ch!='#':
#         ch
#         fp.write(ch)
#         stdout.write(ch)
#         ch = input('')
#     fp.close()
# # 输入文件名：
# # test_file.txt
# # 输入字符串：
# # hahaha
# # hahaha
# # 66666
# # 66666
# # niupi
# # niupi

if __name__ == '__main__':
    filename = input("输入文件名：\n")
    fp = open(filename, "w+")
    ch = ''
    while '#' not in ch:
        fp.write(ch)
        ch = input('输入字符串：\n')
    fp.close()
