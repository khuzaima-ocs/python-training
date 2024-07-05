from math import sqrt, factorial
from random import random, choice, randint

num = 16
num2 = sqrt(num)
print(f'Square root of {num} is {num2}')

num = 6
num2 = factorial(num)
print(f'Factorial of {num} is {num2}')

list = [1,2,3,4,5,6,7]

print("Some random number : " + str(random()))
print("Some random number b/w 10 and 20 : " + str(randint(10,20)))
print("Random choice from list : " + str(choice(list)))