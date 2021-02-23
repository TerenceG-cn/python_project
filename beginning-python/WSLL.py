# 对象属性的lazy initialize，类实例的属性的惰性初始化
class WidgetShowLazyLoad(object):
    def fetch_complex_attr(self, attrname):
        """可能是比较耗时的操作， 比如从文件读取"""
        return attrname, 'wotianna!'

    def __getattr__(self, name):
        if name not in self.__dict__:
            self.__dict__[name] = self.fetch_complex_attr(name)
        return self.__dict__[name]


if __name__ == '__main__':
    w = WidgetShowLazyLoad()
    print('before', w.__dict__)
    w.lazy_loaded_attr
    print('after', w.__dict__)

# 关于__dict__属性
# 类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类__dict__里的
# int, list, dict等这些常用的数据类型是没有__dict__属性的
