import threading
import time


def worker1():
    print(threading.current_thread().getName(), 'start')
    time.sleep(3)
    print(threading.current_thread().getName(), 'end')


def worker2():
    print(threading.current_thread().getName(), 'start')
    time.sleep(3)
    print(threading.current_thread().getName(), 'start')


if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print('started')