from collections import deque

q = deque()
for i in range(10):
    q.append(i)
    print(f'{i} inserted to queue')

print(q)

for i in range(10):
    x = q.popleft()
    print(f'{x} popped from queue')
