
from random import randint

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def get_primes(li):
    primes = []
    for item in li:
        if is_prime(item):
            primes.append(item)

    return primes

size = randint(10,30)
A = []

for i in range(size):
    A.append(randint(1, 1000))

primes = get_primes(A)
print(A)
print(primes)