from abc import ABCMeta, abstractmethod

class IBookData(metaclass = ABCMeta):

    @staticmethod
    @abstractmethod
    def get_book_info():
        pass