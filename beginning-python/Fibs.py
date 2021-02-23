class FIbs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


fibs = 0
fibs = FIbs()
print(type(fibs))
# print(fibs.__next__())
# print(fibs.__iter__())
for f in fibs:
    if f > 1000:
        print(f)
        break
