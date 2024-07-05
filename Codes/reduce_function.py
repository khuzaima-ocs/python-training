from functools import reduce
from random import randint

A = []
for i in range(randint(10,20)):
    A.append(randint(0,100))

def get_max():
    global A
    max_number = reduce(lambda x,y: x if(x>y) else y, A)
    return max_number

print(A)
print(f"Max in this array is {get_max()}")