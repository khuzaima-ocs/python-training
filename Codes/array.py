array = [1,21,42,45,5,26,17,38,9,10]
max_in_array = array[0]
for num in array:
    if num > max_in_array:
        max_in_array = num

print(f'Maximum element in this array is {max_in_array}')