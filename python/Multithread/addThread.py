import threading
'''
threading.active_count() # 获取已经激活的线程数量
threading.enumerate()    # 查看所有线程的信息
threading.current_thread() # 查看正在运行的线程
'''
def thread_job():
	print('This is a thread of %s' % threading.current_thread())

def main():
	thread = threading.Thread(target=thread_job,) # 定义线程
	thread.start() # 让线程开始工作

if __name__ == '__main__':
	main()

