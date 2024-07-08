# FACTORY DESIGN PATTERN

from abc import ABCMeta, abstractmethod

class Person:
    def __init__(self, name, credit_card_ammount, paypal_ammount, bitcoin_ammount):
        self.name = name
        self.credit_card_ammount = credit_card_ammount
        self.paypal_ammount = paypal_ammount
        self.bitcoin_ammount = bitcoin_ammount

class IPayment(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def process_payment(person , amount):
        pass

class CreditCardPaymentProcessor(IPayment):
    def process_payment(self, person: Person, amount):
        if person.credit_card_ammount > amount:
            person.credit_card_ammount -= amount
            print(f"Balance left in credit card: {person.credit_card_ammount}")
        else:
            print("Insufficient balance in your credit card. Try another payment method")

        
class PayPalPaynentProcessor(IPayment):
    def process_payment(self, person: Person, amount):
        if person.paypal_ammount > amount:
            person.paypal_ammount -= amount
            print(f"Balance left in paypal account: {person.paypal_ammount}")
        else:
            print("Insufficient balance in your paypal account. Try another payment method")

class BitcoinPaymentProcessor(IPayment):
    def process_payment(self, person: Person, amount):
        if person.bitcoin_ammount > amount:
            person.bitcoin_ammount -= amount
            print(f"Balance left in bitcoin account: {person.bitcoin_ammount}")
        else:
            print("Insufficient balance in your bitcoin account. Try another payment method")


class PaymentFactory:
    @staticmethod
    def initialize_payment(choice: str):
        if choice.upper() == 'C':
            return CreditCardPaymentProcessor()
        
        if choice.upper() == 'P':
            return PayPalPaynentProcessor()
        
        if choice.upper() == 'B':
            return BitcoinPaymentProcessor()
        
        print("Invalid choice..")
        return -1
    
if __name__ == "__main__":
    p1 = Person("Khuzaima", 4500, 12000, 60)
    choice = input(
"""Enter paymen method
Credit Card (C):   
PayPal (P)
Bitcoin (B): """)
    
    amount = int(input("Enter ammount: "))
    payment = PaymentFactory.initialize_payment(choice)
    if payment != -1:
        payment.process_payment(p1, amount)