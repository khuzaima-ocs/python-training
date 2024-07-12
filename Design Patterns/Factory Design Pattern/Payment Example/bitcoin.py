from ipayment import IPayment
from person import Person

class BitcoinPaymentProcessor(IPayment):
    def process_payment(self, person: Person, amount):
        if person.bitcoin_ammount > amount:
            person.bitcoin_ammount -= amount
            print(f"Balance left in bitcoin account: {person.bitcoin_ammount}")
        else:
            print("Insufficient balance in your bitcoin account. Try another payment method")
