from threading import Thread
from time import sleep

def index():
    for i in range(1,5):
        sleep(3)
        print("1 thread")

def index1():
    for i in range(1,5):
        sleep(8)
        print("2 thread")

t1=Thread(target=index)
t2=Thread(target=index1)

t1.start()
t2.start()

t1.join()
t2.join()

def index3():
    for i in range(1,5):
        sleep(3)
        print("BMW")

def index4():
    for i in range(1,5):
        sleep(5)
        print("Ford")

t3=Thread(target=index3)
t4=Thread(target=index4)

t3.start()
t4.start()

