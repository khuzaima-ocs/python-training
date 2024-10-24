from icecream import ic #pip install icecream
from random import choice

def unpredictable_operation(*args):
    if len(args) < 2 or len(args) > 10:
        raise ValueError("Function requires between 2 and 10 arguments.")
    
    result = args[0]
    
    for arg in args[1:]:
        operation = choice(['+', '-', '*', '/'])
        
        if operation == '+':
            ic()
            result += arg
        elif operation == '-':
            result -= arg
        elif operation == '*':
            result *= arg
        elif operation == '/':
            if arg != 0:
                result /= arg
            else:
                result += arg

    return result

ic(unpredictable_operation(1,2,3,4,5,6,7,8,9,10))
ic(unpredictable_operation(1,2,3,4))
ic(unpredictable_operation(1,2,3,4,5))
ic(unpredictable_operation(1,2,3,4,5))
ic(unpredictable_operation(1,2,3))
ic(unpredictable_operation(1,2,3,4,5,6,7))
ic(unpredictable_operation(1,2,3,4,5,6,7,8,9))