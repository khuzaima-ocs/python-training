import threading
import time

path = "text.txt"
text = ""

def read_file():
    global text, path
    while True:
        with open(path, "r") as f:
            text = f.read()

        time.sleep(1)

def print_text():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=read_file, daemon = True)
t2 = threading.Thread(target=print_text)

t1.start()
t2.start()
