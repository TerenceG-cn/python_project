class MyException(Exception):  # 继承异常类
    def __init__(self, name, reason):
        self.name = name
        self.reason = reason


def factorial(a, b=0):
    # print(a,b)
    try:
        if a > b:
            return a * factorial(a - 1, b)
        elif a==b and b!=0:
            return b
        elif a == 0:
            return 1
        elif a < b:
            return 1
        elif a < b or b < 0:
            raise MyException("IllegalParamsException", "Param is illegal...")
    except MyException as e:
        print(e.name + ":" + e.reason)


def C(n,r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))


# print(C(23,10))

count=0
size=1000000
for n in range(1,101):
    for r in range(1,n+1):
        if C(n,r)>size:
            count+=1
print(count)
