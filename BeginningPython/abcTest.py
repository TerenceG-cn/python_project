from BeginningPython import abcDemo


# Talker()

class Knight(abcDemo.Talker):
    def talk(self):
        print("Ni")


class Herring():
    def talk(self):
        print("Blub")


# k = Knight()
# isinstance(k, Talker)
# k.talk()
h = Herring()
print(isinstance(h, Talker))

Talker.register(Herring)
print(isinstance(h, Talker))
print(issubclass(h, Talker))
