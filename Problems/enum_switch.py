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

from enum import Enum, auto

class CoffeeTypes(Enum):
    ESPRESSO = auto()
    LATTE = auto()
    CAPPUCCINO = auto()
    AMERICANO = auto()
    MOCHA = auto()

def process_order(order: list):
    total_bill = 0
    
    for item in order:
        
        match CoffeeTypes[item["name"].upper()]:
            case CoffeeTypes.ESPRESSO:
                total_bill += 3.0 * item["quantity"]

            case CoffeeTypes.LATTE:
                total_bill += 4.0 * item["quantity"]

            case CoffeeTypes.CAPPUCCINO:
                total_bill += 4.5 * item["quantity"]

            case CoffeeTypes.AMERICANO:
                total_bill += 2.5 * item["quantity"]

            case CoffeeTypes.MOCHA:
                total_bill += 5.0 * item["quantity"]

    print(f"TOTAL BILL:     ${total_bill}")

    
process_order([{"name": "ESPRESSO", "quantity" : 2}, {"name" : "LATTE", "quantity" : 10}, {"name" : "MOCHA", "quantity" : 1}])
