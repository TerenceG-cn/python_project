from operator import *

person = {"zli": 18, "wang": 59, "ihang": 20, "sun": 22}


def find_max(dict):
    max_age = 0
    for key, value in dict.items():
        if value > max_age:
            max_age = value
            name = key
    print(name)
    print(max_age)


def find_max2(dict):
    key_maxValue = sorted(dict.items(), key=lambda item: item[1], reverse=True)[0]
    print(key_maxValue)  # 获取最大值


find_max2(person)
