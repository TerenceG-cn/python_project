# 列表转换为字典

i = ['a', 'b']
ll = [1, 2]

print(dict(zip(i, ll)))
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
# 我们可以使用 list() 转换来输出列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

# dict()使用实例，参数如何表示一个键值对
dict0 = dict()  # 传一个空字典
print('dict0:', dict0)

dict1 = dict({'three': 3, 'four': 4})  # 传一个字典
print('dict1:', dict1)

dict2 = dict(five=5, six=6)  # 传关键字
print('dict2:', dict2)

dict3 = dict([('seven', 7), ('eight', 8)])  # 传一个包含一个或多个元祖的列表 tuple
print('dict3:', dict3)

dict5 = dict(zip(['eleven', 'twelve'], [11, 12]))  # 传一个zip()函数
print('dict5:', dict5)

dict6 = dict([['wu', 'liu'], [5, 6]])  # 错误示范
print('dict6:', dict6)
