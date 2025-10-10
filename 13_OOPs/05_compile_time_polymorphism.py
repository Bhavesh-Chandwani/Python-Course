# Python does not support compile time polymorphism directly. It mimics using default argumnents or *args/**kwargs

class Calculator:
    def add(self, *args):
        return sum(args)
c = Calculator()
print(c.add(5,6))
print(c.add(5,6,7))
print(c.add(5,6,7,8,9))