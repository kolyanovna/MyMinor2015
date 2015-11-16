__author__ = 'NikolaiEgorov'

class MyClass:
    """A simple class"""
    name = ""
    i = 12345
    j = i
    def __init__(self, name = "Defaul Name"):
        self.i = 0
        self.name = name

instance1 = MyClass()
print(instance1.i)
print(instance1)
print(instance1.j)
print(instance1.__doc__)
print(instance1.name)
print(dir(instance1))
# динамическое добавление в класс
instance1.NEW = "Новое поле"
print(instance1.NEW)
# нельзя удалить объект изначально в классе
print(dir(instance1))
del instance1.NEW
print(dir(instance1))
del instance1

