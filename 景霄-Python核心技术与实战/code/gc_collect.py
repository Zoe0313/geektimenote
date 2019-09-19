"""
循环引用的垃圾回收也可以用gc.collect()
"""

import os
import psutil
import gc

# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))

def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info('after a, b created')
    a.append(b)
    b.append(a)

func()
gc.collect()
show_memory_info('finished')

########## 输出 ##########
# initial memory used: 5.9609375 MB
# after a, b created memory used: 646.95703125 MB
# finished memory used: 9.40234375 MB
