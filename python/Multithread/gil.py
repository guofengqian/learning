'''
gil: global interpreter lock
它确保任何时候都只有一个python线程执行。
它使python的多线程并不能利用多核CPU的优势。

它只会影响到那些严重依赖CPU的程序（比如计算型的）。
比如网络交互，那么使用多线程就很合适。因为他们大部分时间都在等待。
'''
import threading
from queue import Queue
import copy
import time

def job(l,q):
	res = sum(l)
	q.put(res)

def multithreading(l):
	q = Queue()
	threads = []
	for i in range(4):
		t = threading.Thread(target=job, args = (copy.copy(l), q), name='T%i' % i)
		t.start()
		threads.append(t)
	[t.join() for t in threads]
	total = 0
	for _ in range(4):
		 total += q.get()
	print(total)

def normal(l):
	total = sum(l)
	print(total)

if __name__ == '__main__':
	l = list(range(1000000))
	s_t = time.time()
	normal(l*4)
	print('normal: ',time.time() - s_t)
	s_t = time.time()
	multithreading(l)
	print('multithreading: ', time.time() - s_t)
