"""
Write a function that returns some of the digits of a number until it becomes a single digit
Number: 123456
Explanation: Sum of digits is 21 but its a 2 digit number so we will number these digits
Return value = 3
"""

def sum_digits(num):
    while num > 9:
        sum = 0
        num_copy = num
        while num_copy >= 1:
            sum += num_copy % 10
            num_copy //= 10

        num = sum

    return sum

print(sum_digits(765432198))