with open('demo_tell.txt', 'w+') as f:
    x = input("Enter your name: ")
    f.write(x)

    position = f.tell()
    print(f"Position of Pointer: {position}")
    f.seek(9)
    position = f.tell()
    print(f"Position of Pointer: {position}")
    print(f.read())
    position = f.tell()
    print(f"Position of Pointer: {position}")
    