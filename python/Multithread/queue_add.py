'''
将数据列表中的数据传入，使用四个线程处理，将结果保存在
queue中，线程执行完后，从queue中获取存储的结果

'''
import threading
import time

from queue import Queue

def job(l,q):
	for i in range(len(l)):
		l[i] = l[i]**2
	q.put(l)

def multithreading():
	q = Queue()
	threads = []
	data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
	for i in range(4):
		t = threading.Thread(target=job, args=(data[i],q))
		t.start()
		threads.append(t)
	for thread in threads:
		thread.join()
	results = []
	for _ in range(4):
		results.append(q.get())
	print(results)

if __name__ == '__main__':
	multithreading()
