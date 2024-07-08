import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:],"f:m:",["filename","message"])

filename = ""
message = ""

for opt, arg in opts:
    if opt == "-f":
        filename = arg
    
    if opt == "-m":
        message = arg


if filename != "":
    with open(filename, "w+") as f:
        f.write(message)
else:
    print("Filename not provided")