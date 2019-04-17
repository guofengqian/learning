import multiprocessing as mp
import time

def job(v, num):
	for _ in range(5):
		time.sleep(0.1) # 暂停0.1s，让输出效果更明显
		v.value += num  # v.value获取共享变量值
		print(v.value,end="\n")

def multicore():
	v = mp.Value('i',0) # 定义共享变量
	p1 = mp.Process(target=job,args=(v,1))
	p2 = mp.Process(target=job,args=(v,3))
	p1.start()
	p2.start()
	p1.join()
	p2.join()

if __name__ == '__main__':
	multicore()
