__author__ = 'NikolaiEgorov'


class Point():
    # вызывается при удалении
    def __del__(self):
        print("something")


class Parent:
    def __init__(self):
        self.name = "parent"

    def myMethod(self):
        print("Parent method")

    name = ""


class Child(Parent):
    child = ""

    def myMethod(self):
        print("Child method")

    def __init__(self):
        super().__init__()
        self.name = "child"


man = Parent()
print(man.myMethod())
man = Child()
print(man.myMethod())
