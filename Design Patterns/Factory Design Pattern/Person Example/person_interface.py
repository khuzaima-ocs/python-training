from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def display():
        pass