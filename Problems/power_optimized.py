# Time Complexity: O(lgN) where N is the power (exp).

def power(base, exp):
    
    def power_inner(base, exp):

        if exp == 1:
            return base
    
        result = power_inner(base, exp // 2)
        
        if exp % 2 == 0:
            return result * result
        else:
            return result * result * base

    if exp == 0:
        return 1
    
    elif exp > 0:
        return power_inner(base, exp)

    else: # Negative Power
        return power_inner(1/base, -1 * exp)
