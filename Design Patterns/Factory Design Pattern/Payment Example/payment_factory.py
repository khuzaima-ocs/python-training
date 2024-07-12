from credit_card import CreditCardPaymentProcessor
from paypal import PayPalPaynentProcessor
from bitcoin import BitcoinPaymentProcessor

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