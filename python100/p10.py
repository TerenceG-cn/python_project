# 格式化当地时间
import time

print(time.strftime('%Y-%m-%d %H:%H:%S', time.localtime(time.time())))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%H:%S', time.localtime(time.time())))
