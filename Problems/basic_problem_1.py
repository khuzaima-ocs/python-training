"""
Write a function that returns the intersection of 2 arrays (of unique elements).
Try to solve the problem in O(n)
"""

array_1 = [3,1,9,7,4]
array_2 = [3,2,9,12,6]

def intersect(A1, A2):
    frequency = {}
    
    for item in A1 + A2:
        frequency[item] = frequency.get(item, 0) + 1

    result = []
    for key in frequency:
        if frequency[key] > 1:
            result.append(key)

    return result

res = intersect(array_1, array_2)
print(res)