import threading
import time

event = threading.Event()

def func():
    print("Entered function\n")
    event.wait()
    print("Function execution completed")

t1 = threading.Thread(target=func)
t1.start()

x = input("Enter 'y' to complete function execution: \n").upper()
if x == 'Y':
    event.set()
