"""
Write a function that return the binary of a decimal number
Note: We don't have string & array data types so you can only use Integar
"""

def reverse_binary(number):
    reverse = 0

    while number > 1:
        remainder = number % 2
        reverse = (reverse * 10) + remainder

        number //= 10

    reverse = (reverse * 10) + number

    return reverse

def dec_to_bin(decimal):
    binary = 0
    zeros_at_start = 0
    while decimal > 1:
        remainder = decimal % 2
        if binary == 0 and remainder == 0:
            zeros_at_start += 1

        binary = (binary * 10) + remainder
        decimal //= 2
    binary = (binary * 10) + decimal

    result = reverse_binary(binary)

    for _ in range(zeros_at_start):
        result = (result * 10) + 0

    return result

for i in range(100):
    res = dec_to_bin(i)
    print(f"{i} : {res}")
