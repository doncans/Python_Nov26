from multiprocessing import Process

from threading import Thread
import time
def sqr(n):
    for i in range(n):
        print(i*2)
def cube(n):
    for i in range(n):
        print(i*3)
print("Thread ended")

t_start = time.time()
t1 = Thread(target=sqr, args=(100000,))
t2 = Thread(target=cube, args=(100000,))
t1.start()
t2.start()
t1.join()
t2.join()
print("time took multithread : "+ str(time.time()-t_start))


