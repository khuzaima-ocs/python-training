from collections import deque

stack = deque()
for i in range(10):
    stack.append(i)
    print(f'{i} inserted to stack')

print(stack)

for i in range(10):
    x = stack.pop()
    print(f'{x} popped from stack')
