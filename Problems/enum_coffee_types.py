""" 
You are tasked with developing an advanced order processing system for a coffee shop. 
The system should handle orders for different types of coffee, calculate the total price, 
preparation time, and apply discounts for bulk orders.

Espresso: Price = $3.00, Preparation Time = 2 minutes
Latte: Price = $4.00, Preparation Time = 4 minutes
Cappuccino: Price = $4.50, Preparation Time = 3 minutes
Americano: Price = $2.50, Preparation Time = 3 minutes
Mocha: Price = $5.00, Preparation Time = 5 minutes
"""

from enum import Enum

class CoffeeTypes(Enum):
    ESPRESSO = {"price": 3.0, "prep_time": 2}
    LATTE = {"price": 4.0, "prep_time": 4}
    CAPPUCCINO = {"price": 4.0, "prep_time": 3}
    AMERICANO = {"price": 2.5, "prep_time": 3}
    MOCHA = {"price": 5.0, "prep_time": 5}

class Discounts(Enum):
    FIVE_PERCENT = 5.0
    TEN_PERCENT = 10.0

def process_order(order: list):
    total_bill, total_time, total_qnty  = 0, 0, 0
    
    for item in order:
        coffee = CoffeeTypes[item["name"].upper()]
        total_bill += coffee.value['price'] * item["quantity"]
        total_time = max(total_time, coffee.value["prep_time"]) 
        total_qnty += item["quantity"]

    discount = apply_discount(total_qnty)

    return total_bill, total_time, total_qnty, discount,

def apply_discount(qnty):
    discount = 0
    if qnty > 20:
        discount = Discounts.TEN_PERCENT.value
    
    elif qnty > 10:
        discount = Discounts.FIVE_PERCENT.value
    
    return discount

def print_bill(order):
    total_bill, total_time, total_qnty, discount = order
    print(f"""
TOTAL TIME:     {total_time}
TOTAL QUANTITY: {total_qnty}
          
TOTAL BILL:     ${total_bill}
DISCOUNT:       ${discount}
TOTAL PAYABLE:  ${total_bill - discount}
""")
        
order = process_order([{"name": "ESPRESSO", "quantity" : 2}, {"name" : "LATTE", "quantity" : 10}, {"name" : "MOCHA", "quantity" : 1}])
print_bill(order)