from abc import ABCMeta, abstractmethod

class IPayment(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def process_payment(person , amount):
        pass