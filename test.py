"""
Создать метод класса get_counter. Создать три объекта класса.
Вызвать через класс метод get_counter.
"""
class Counter:
    __counter_cls: int
    __counter_self:int

    def __init__(self, counter):
        self.__counter_self = counter
        Counter.__counter_cls = counter

    @classmethod
    def get_counter(cls):
        print("Метод класса get_counter")
        return cls.__counter_cls

c1 = Counter(10)

print(Counter.get_counter())

class Counter2:
    #__counter_cls: int
    __counter_self:int

    def __init__(self, counter):
        self.__counter_self = counter
        #Counter.__counter_cls = counter

    #@classmethod
    def get_counter(self):
        print("Метод класса get_counter")
        return self.__counter_self

c2 = Counter2(20)

print(c2.get_counter())
print(Counter2.get_counter())