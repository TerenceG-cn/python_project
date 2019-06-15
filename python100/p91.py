# 时间函数举例

if __name__ == '__main__':
    import time

    print(time.ctime(time.time()))  # Python time time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
    print(time.clock())
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))
