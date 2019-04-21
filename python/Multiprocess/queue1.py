'''
环境：python3

 Queue是将每个核或线程的运算结果放在队里，等到
 每个线程或核运行完毕后再从队列里取出结果，继续
 加载运算，因为多线程调用的函数不能有返回值，所
 一使用Queue存储多个线程运算的结果

注意：在当前目录下，不能有名字为"queue.py"的文件，不然会
      报错：
ImportError: cannot import name 'Empty' from 'queue' (/Users/qiankokufeng/Documents/learning/python/Multiprocess/queue.py)
'''
import multiprocessing as mp

def job(q,m):
	res = 'none' 
	if m == 1:
		res = 'I am res1' 
	else:
		res = 'I am res2'
	q.put(res)

if __name__ == '__main__':
	q = mp.Queue()
	p1 = mp.Process(target=job,args=(q,1))
	p2 = mp.Process(target=job,args=(q,2))
	
	p1.start()
	p2.start()
	p1.join()
	p2.join()

	res1 = q.get()
	res2 = q.get()

	print(res1)
	print(res2)
