from threading import Thread
import time


class Hello(Thread):
    def run(self):
        for _ in range(5):
            print("Hello")
class Hi(Thread):
    def run(self):
        for _ in range(5):
            print("Hi")

if __name__=="__main__":
    t1 = Hello()
    t2 = Hi()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

print("Thread ended")

# def sqr(n):
#     for i in range(n):
#         print(i*2)
# def cube(n):
#     for i in range(n):
#         print(i*3)
#
# # sqr(10)
# # cube(10)
# t1 = Thread(target=sqr, args=(10,))
# t2 = Thread(target=cube, args=(10,))
# start_time = time.time()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end_time = time.time()
#
# print(end_time-start_time)
