'''
总结：pool默认调用是CPU全部的内核，传入processes参数可自定义内核数量
	  map()放入迭代参数(0,1,2,)，返回多个结果
	  apply_async只能放入一个参数，并返回一个结果，如果想得到map()
	的效果需要通过迭代(i,) for i in range(3)
'''
import multiprocessing as mp

def job(x):
	return x*x

# map会放入processes个内核中去进行运算
def map_multicore():
	pool = mp.Pool(processes=2) # 定义CPU核的数量是2
	while True:
		# 传入值需要是可迭代的，所以在传入值后需要加逗号
		res = pool.map(job, range(10)) # 往进程池里丢入任务job
	print(res)
	
# apply_async只会放入一个核进行运算，但实际上所有核都被使用
# 并不清楚怎么回事
def apply_async_multicore():
	pool = mp.Pool()
	while True:
		# 传入值需要是可迭代的，所以在传入值后需要加逗号
		# 但是却只能传入一个参数，跟map不一样，
		# 同时在取出时，需要用get()方法一个个取出来
		res = pool.apply_async(job, (i,) for i in range(10))
	print(res.get() for res in res)

if __name__ == '__main__':
	apply_async_multicore()
