from multiprocessing import Process
import time
def sqr(n):
    print(n*n)
def cube(n):
    print(n*n*n)

# sqr(10)
# cube(10)
if __name__=="__main__":	
	start_time = time.time()
	p1 = Process(target=sqr, args=(1000,))
	p2 = Process(target=cube, args=(1000,))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	print("time took multiprocess: "+ str(time.time()-start_time))