from random import randint

A = []
for i in range(randint(10,20)):
    A.append(randint(0,100))

def get_greater_than_fifty():
    global A
    A = list(filter(lambda x : x>50, A))

print(A)
get_greater_than_fifty()
print(A)