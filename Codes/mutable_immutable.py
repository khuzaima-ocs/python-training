print("Arrays and dictionaries are mutable. We can change them")
array = [1,2,3,4,5]
array[0] = 10
print(array)

dict = {
    'a' : 1,
    'b' : 3
}
dict['a'] = 2
print(dict)

print("Strings and tuples are immutable. We cannot change their values")
string = "Hello World"
string[0] = 'J' # Error
print(string)

tuple = (1,0)
tuple[0] = 2 # Error
print(tuple)