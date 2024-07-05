def find_max(array):
    max_el = array[0]
    for num in array:
        max_el = max(max_el, num)
    return max_el


def find_min(array):
    min_el = array[0]
    for num in array:
        min_el = min(min_el, num)
    return min_el

def calculate_avg(array):
    sum = 0
    for num in array:
        sum += num

    return sum / len(array)

array = [10,18,6,99,76,58,15]

max_in_array = find_max(array)
min_in_array = find_min(array)
avg = calculate_avg(array)

print(f"Average of Array is : {avg}")
print(f'Maximum element in array is : {max_in_array}')
print(f'Minimum element in array is : {min_in_array}')

