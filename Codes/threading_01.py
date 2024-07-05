import threading
import time


def fun1():
    for i in range(10):
        time.sleep(1)
        print(i)

def fun2():
    for i in range(20,30):
        time.sleep(2)
        print(i)


t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)

t1.start()
t2.start()

t1.join()
print("T1 ended execution")
