from person import Person
from payment_factory import PaymentFactory

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