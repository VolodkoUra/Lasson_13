"""
Создать метод класса get_counter. Создать три объекта класса.
Вызвать через класс метод get_counter.
"""

class Counter:
    __counter: int
    def __init__(self, counter):
        self.__counter = counter
        Counter.__counter = counter

    @classmethod
    def get_counter(cls):
        return cls.__counter

c1 = Counter(5)



print(Counter.get_counter())
c2 = Counter(10)
print(Counter.get_counter())
c3 = Counter(15)
print(Counter.get_counter())