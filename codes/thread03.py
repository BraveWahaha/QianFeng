#全局变量计算量较大的情况
import threading
from time import sleep

n = 0
lock = threading.Lock()
def task1():
    lock.acquire()
    global n
    for i in range(1000000):
        n += 1
    print('task1中n的值为：------',n)
    lock.release()

def task2():
    lock.acquire()
    global n
    for i in range(1000000):
        n += 1
    print('task2中n的值为：------',n)
    lock.release()

if __name__ == '__main__':
    th1 = threading.Thread(target=task1)
    th2 = threading.Thread(target=task2)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print('最后n的值为：',n)