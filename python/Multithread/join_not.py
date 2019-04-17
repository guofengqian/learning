import threading
import time

def thread_job():
	print('T1 start\n')
	for i in range(10):
		time.sleep(0.1) # 任务间隔0.1s
	print('T1 finish\n')

added_thread = threading.Thread(target=thread_job, name='T1')
added_thread.start()
print("all done\n")
