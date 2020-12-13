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
t1 = Thread(target=sqr, args=(10,))
t2 = Thread(target=cube, args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()
print("time took multithread : "+ str(time.time()-t_start))
def sqr(n):
    for i in range(n):
        print(i*2)
def cube(n):
    for i in range(n):
        print(i*3)

# sqr(10)
# cube(10)
p1 = Process(target=sqr, args=(10,))
p2 = Process(target=cube, args=(10,))
start_time = time.time()
p1.start()
p2.start()
p1.join()
p2.join()
print("time took multiprocess: "+ str(time.time()-start_time))

