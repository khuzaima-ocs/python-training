import sys

with open("demo.txt") as f:
    x = f.readline()
    sys.stdout.write(x)
    sys.stderr.write("No error occured..!!")