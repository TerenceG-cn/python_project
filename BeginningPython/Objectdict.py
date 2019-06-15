# 像访问属性一样访问dict中的键值对
class ObjectDict(dict):
    def __init__(self, *args, **kwargs):
        super(ObjectDict, self).__init__(*args, **kwargs)

    def __getattr__(self, name):
        value = self[name]
        if isinstance(value, dict):
            value = ObjectDict(value)
        return value


if __name__ == '__main__':
    od = ObjectDict(arg0={'a': 1}, arg1=True)
    # print(od.asf, od.asf.a)  # {'a': 1} 1
    print(od.arg1)  # True
    print(od.arg0, od.arg0.a)
