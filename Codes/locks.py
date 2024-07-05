import threading
import time

lock = threading.Lock()

def func(thread_no):
    print("Function started by thread " + str(thread_no))
    lock.acquire()
    print("Lock acquired by thread " + str(thread_no))
    time.sleep(3)
    lock.release()
    print("Lock released by thread " + str(thread_no))

t1 = threading.Thread(target=func, args=(1, ))
t2 = threading.Thread(target=func, args=(2, ))
t3 = threading.Thread(target=func, args=(3, ))

t1.start()
t2.start()
t3.start()