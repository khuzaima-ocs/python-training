def prime_finder_vanilla(amount):

    number = 2
    found = 0

    primes = []

    while found < amount:
        for x in primes:
            if number % x == 0:
                break
        
        else:
            primes.append(number)
            found += 1
        
        number += 1

    return primes
            

def prime_finder_optimized(int amount):

    cdef int number, found, x
    cdef int primes[100000]

    number = 2
    found = 0

    while found < amount:
        for x in primes[:found]:
            if number % x == 0:
                break
        
        else:
            primes[found] = number
            found+=1

        number += 1

    
    return primes