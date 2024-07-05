from random import randint

A = []
for i in range(randint(10,20)):
    A.append(randint(0,100))

# This function will make each element of list divisible by 10
# 87 -> 80
# 53 -> 50
# 20 -> 20
def make_last_digit_zero():
    global A
    A = list(map(lambda x: x - (x % 10), A))

print(A)
make_last_digit_zero()
print(A)