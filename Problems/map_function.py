from random import randint

def double(A):
    return list(map(lambda x: x*2, A))

size = randint(10,30)
A = []

for i in range(size):
    A.append(randint(1, 1000))

output = double(A)

print(A)
print(output)