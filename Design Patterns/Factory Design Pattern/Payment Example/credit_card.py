from ipayment import IPayment
from person import Person

class CreditCardPaymentProcessor(IPayment):
    def process_payment(self, person: Person, amount):
        if person.credit_card_ammount > amount:
            person.credit_card_ammount -= amount
            print(f"Balance left in credit card: {person.credit_card_ammount}")
        else:
            print("Insufficient balance in your credit card. Try another payment method")
