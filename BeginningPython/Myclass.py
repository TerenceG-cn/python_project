from BeginningPython.Rectangle import Rectangle


class Myclass:

    def smeth():
        print('This is a static method')

    smeth = staticmethod(smeth)

    def cmeth(cls):
        print('This is a class method of', cls)

    cmeth = classmethod(cmeth)


cls = Rectangle()
Myclass.cmeth()
Myclass.smeth()
