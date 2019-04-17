'''
lock()的作用：在当前线程没有运行完毕时，不允许其它线程对它操作的
共享变量进行操作
'''
import threading 

def job1():
	global A,lock
	lock.acquire()
	for i in range(10):
		A += 1
		print('job1',A)
	lock.release()
	
def job2():
	global A,lock
	lock.acquire()
	for i in range(10):
		A += 10
		print('job2',A)
	lock.release()

if __name__ == '__main__':
	lock=threading.Lock()
	A = 0
	t1 = threading.Thread(target=job1)
	t2 = threading.Thread(target=job2)
	t1.start()
	t2.start()
	t1.join() 
	t2.join()# join使得主线程"处于阻塞状态，直到子进程t1和t2运行结束
	A += 20
	print("main finish!")
	
