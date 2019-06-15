# 字符串日期转换为易读的日期格式。

from dateutil import parser

dt = parser.parse("Aug 28 2015 12:00AM")  # 直接将字符串转换为datetime格式
print(dt)
