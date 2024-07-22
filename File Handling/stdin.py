import sys
with open("stdin_demo.txt", 'a') as f:
    for line in sys.stdin:
        if 'q' == line.rstrip():
            break
        
        print(f"Input: {line}")
        f.write(line)

# Default 'Reading Mode'
with open("stdin_demo.txt") as f:
    print(f.read())