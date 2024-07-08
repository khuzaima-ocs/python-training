def generator():
    res = 1
    while True:
        yield res
        res *= 5


values = generator()
for i in range(100):
    print(next(values))