"""
Write a function that returns the intersection of 2 arrays.
Try to solve the problem in O(n)
"""

array_1 = [3,1,9,7,4]
array_2 = [3,2,9,12,6]

def intersect(A1, A2):
    hashmap = {}
    
    for item in A1 + A2:
        hashmap[item] = hashmap.get(item, 0) + 1

    result = []
    for key in hashmap:
        if hashmap[key] > 1:
            result.append(key)

    return result

res = intersect(array_1, array_2)
print(res)