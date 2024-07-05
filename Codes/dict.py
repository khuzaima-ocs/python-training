text = "Hello buddy, my name is Khuzaima"
frequency = {}

for c in text:
    frequency[c] = frequency.get(c, 0) + 1

print(frequency)
