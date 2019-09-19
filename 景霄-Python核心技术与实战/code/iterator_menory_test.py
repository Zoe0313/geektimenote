import os
import psutil

# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)
    
    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))

def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]#生成一个包含一亿元素的列表
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')

def test_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(100000000))#初始化了一个生成器
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')

%time test_iterator()
%time test_generator()

########## 输出 ##########

# initing iterator memory used: 48.9765625 MB
# after iterator initiated memory used: 3920.30078125 MB
# 4999999950000000
# after sum called memory used: 3920.3046875 MB
# Wall time: 17 s
# initing generator memory used: 50.359375 MB
# after generator initiated memory used: 50.359375 MB
# 4999999950000000
# after sum called memory used: 50.109375 MB
# Wall time: 12.5 s
