import threading

money = 1000

def run1():
    global money
    for i in range(100):
        money -= 1

def run2():
    global money
    for i in range(100):
        money -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target=run1)
    t2 = threading.Thread(target=run1)
    t3 = threading.Thread(target=run1)
    t4 = threading.Thread(target=run1)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    print('money:',money)
    print('test the pull operation')
