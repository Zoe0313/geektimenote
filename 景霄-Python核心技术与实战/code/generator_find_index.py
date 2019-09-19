#给定一个list和一个指定数字，求这个数字在list中的位置
"""
在Python语言规范中，用更少、更清晰的代码实现相同功能，一直是被推崇的做法，
因为这样能够很有效提高代码的可读性，减少出错概率，也方便别人快速准确理解你的意图。
当然，要注意，这里“更少”的前提是清晰，而不是使用更多的魔术操作，
虽说减少了代码却反而增加了阅读的难度。
"""


#方法一：
def index_normal(L, target):
    result = []
    for i, num in enumerate(L):
        if num == target:
            result.append(i)
    return result

print(index_normal([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2))

########## 输出 ##########
#[2, 5, 9]


#方法二：
def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i

print(list(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))

########## 输出 ##########
#[2, 5, 9]
