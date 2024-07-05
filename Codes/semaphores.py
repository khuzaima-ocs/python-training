import threading
import time

semaphore = threading.BoundedSemaphore(5)

def func(thread_no):
    print(f'Function started by thread {thread_no}')
    semaphore.acquire()
    print(f'Thread {thread_no} acquired')
    time.sleep(2)
    semaphore.release()
    print(f'Thread {thread_no} released')

for i in range(10):
    t = threading.Thread(target=func, args=(i,))
    time.sleep(1)
    t.start()