
def is_multiple_of_two(num):
    return num > 1 and not (num & num-1)

def double(num, times = 1):
    return num << times

def half(num, times = 1):
    return num >> times

for i in range(1000):
    if is_multiple_of_two(i):
        print(f"{i} is multiple of 2")

print(double(100, 4))
print(half(100, 4))

    