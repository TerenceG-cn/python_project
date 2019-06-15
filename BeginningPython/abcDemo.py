from abc import ABC, abstractclassmethod


class Talker(ABC):
    @abstractclassmethod
    def talk(self):
        pass


i = [1, 2, 3]

i.__len__()
