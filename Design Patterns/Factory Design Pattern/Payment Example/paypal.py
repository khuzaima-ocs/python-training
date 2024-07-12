from ipayment import IPayment
from person import Person

class PayPalPaynentProcessor(IPayment):
    def process_payment(self, person: Person, amount):
        if person.paypal_ammount > amount:
            person.paypal_ammount -= amount
            print(f"Balance left in paypal account: {person.paypal_ammount}")
        else:
            print("Insufficient balance in your paypal account. Try another payment method")
