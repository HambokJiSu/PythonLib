#	반드시 메서드를 구현하도록 하려면? ― abc
from abc import ABCMeta, abstractmethod


class Bird(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Eagle(Bird):
    def fly(self):
        print("very fast")


eagle = Eagle()
eagle.fly()