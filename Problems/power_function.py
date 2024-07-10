# Time Complexity: O(N) where N is the power (exp).

def power(base, exp):
    def power_inner(result ,exp):
        nonlocal base

        if exp == 1:
            return result
        
        return power_inner(result * base, exp - 1)

    if exp == 0:
        return 1
    
    elif exp > 0:
        return power_inner(base, exp)

    else: # Negative Power
        base = 1/base
        return power_inner(base, -1 * exp)
    
print(power(10, 10))