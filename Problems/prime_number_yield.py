def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def get_prime():
    i = 2
    while True:
        if is_prime(i):
            yield i
            
        i+=1

n = int(input("How many primes numbers you want: "))
primes = get_prime()
for i in range(n):
    num = next(primes)
    print(num)