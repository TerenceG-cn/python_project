# 在for遍历list时使用remove出现的问题以及解析

numList = [1, 2, 3, 4, 5]

for i in numList:
    numList.remove(i)
    print(numList)
print('----------------------------------')
# 打印结果：
# [2, 3, 4, 5] remove指向1
# [2, 4, 5]  remove指向2
# [2, 4]   remove指向3


nums = [1, 2, 3, 4, 5]
# 第一种办法
# for n in nums.copy():
#     nums.remove(n)
#     print(nums)

# 第二种办法
# numsCopy=[1,2,3,4,5]
# for n in numsCopy:
#     nums.remove(n)
#     print(nums)
