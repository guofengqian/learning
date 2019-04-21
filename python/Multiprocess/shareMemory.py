'''
共享内存：让CPU之间有交流

'''
import multiprocessing as mp

#----- Shared Value -----
# 通过Value把数据存储在一个共享内存表中
# i和d是用来设置数据类型的
# i表示一个带符号的整型
# d表示一个双精度浮点型
value1 = mp.Value('i',0)    
value2 = mp.Value('d',3.14) 

#----- Shared Array -----
# Array类，可以和共享内存交互，实现在进程之间共享数据
# Array是以为数据
# 'i'表示数据类型是signed int
# 更多数据类型在https://docs.python.org/3/library/array.html
array = mp.Array('i',[1,2,3,4])


