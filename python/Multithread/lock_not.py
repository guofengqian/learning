'''
这里没有加lock，但是输出是混乱的，job2和job1交叉着对
全局变量A所在的内存进行操作


'''
import threading 

def job1():
	global A
	for i in range(10):
		A += 1
		print('job1',A)
	
def job2():
	global A
	for i in range(10):
		A += 10
		print('job2',A)

if __name__ == '__main__':
	lock=threading.Lock()
	A = 0
	t1 = threading.Thread(target=job1)
	t2 = threading.Thread(target=job2)
	t1.start()
	t2.start()
#	t1.join()
#	t2.join()
	
