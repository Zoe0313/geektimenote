import numpy as np
persontype = np.dtype({
    'names':['name', 'age', 'chinese', 'math', 'english'],
    'formats':['S32','i', 'i', 'i', 'f']})
peoples = np.array(
    [
        ("ZhangFei",32,75,100,90),
        ("GuanYu",24,85,96,88.5),
        ("ZhaoYun",28,85,92,96.5),
        ("HuangZhong",29,65,85,100)
    ],
    dtype=persontype)

ages = peoples[:]['age']
print(ages)
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))


"""
Numpy可以很方便地创建连续的数组

arange() 类似内置函数 range()，
通过指定初始值、终值、步长来创建等差数列的一维数组，默认是不包括终值的。

linspace 是 linear space 的缩写，代表线性等分向量的含义。
linspace() 通过指定初始值、终值、元素个数来创建等差数列的一维数组，默认是包括终值的。

通过 NumPy 可以自由地创建等差数组，同时也可以进行加、减、乘、除、求 n 次方和取余数。
"""
x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print(x1)
print(x2)
print(np.add(x1, x2))
#等价于 print(x1+x2)
print(np.subtract(x1, x2))
#等价于 print(x1 - x2)
print(np.multiply(x1, x2))
#等价于 print(x1*x2)
print(np.divide(x1, x2))
#等价于 print(x1/x2)
print(np.power(x1, x2))
#等价于 print(x1**x2)
print(np.remainder(x1, x2))
#等价于np.mod(x1, x2)
#等价于 print(x1%x2)

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
"""
amin() 用于计算数组中的元素沿指定轴的最小值。
对于一个二维数组 a，amin(a) 指的是数组中全部元素的最小值，
amin(a,0) 是延着 axis=0 轴的最小值，
axis=0 轴是把元素看成了 [1,4,7], [2,5,8], [3,6,9] 三个元素，
所以最小值为 [1,2,3]，
amin(a,1) 是延着 axis=1 轴的最小值，
axis=1 轴是把元素看成了 [1,2,3], [4,5,6], [7,8,9] 三个元素，
所以最小值为 [1,4,7]。
同理 amax() 是计算数组中元素沿指定轴的最大值。
"""
print(np.amin(a))
print(np.amin(a,0))
print(np.amin(a,1))
print(np.amax(a))
print(np.amax(a,0))
print(np.amax(a,1))
"""
对于相同的数组 a，
np.ptp(a) 可以统计数组中最大值与最小值的差，即 9-1=8。
同样 ptp(a,0) 统计的是沿着 axis=0 轴的最大值与最小值之差，
即 7-1=6（当然 8-2=6,9-3=6，第三行减去第一行的 ptp 差均为 6），
ptp(a,1) 统计的是沿着 axis=1 轴的最大值与最小值之差，
即 3-1=2（当然 6-4=2, 9-7=2，即第三列与第一列的 ptp 差均为 2）。
"""
print(np.ptp(a))
print(np.ptp(a,0))
print(np.ptp(a,1))

"""
统计数组的百分位数

percentile() 代表着第 p 个百分位数，这里 p 的取值范围是 0-100，
如果 p=0，那么就是求最小值，如果 p=50 就是求平均值，如果 p=100 就是求最大值。
同样你也可以求得在 axis=0 和 axis=1 两个轴上的 p% 的百分位数。
"""
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))

# 求中位数
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))
# 求平均数
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

"""
统计数组中的加权平均值

average() 函数可以求加权平均，
加权平均的意思就是每个元素可以设置个权重，
默认情况下每个元素的权重是相同的，
所以 np.average(b)=(1+2+3+4)/4=2.5，
你也可以指定权重数组 wts=[1,2,3,4]，
这样加权平均 np.average(b,weights=wts)=(1*1+2*2+3*3+4*4)/(1+2+3+4)=3.0。
"""
b = np.array([1,2,3,4])
wts = np.array([1,2,3,4])
print(np.average(b))
print(np.average(b,weights=wts))

"""
统计数组中的标准差 std()、方差 var()

方差的计算是指每个数值与平均值之差的平方求和的平均值，
即 mean((x - x.mean())** 2)。
标准差是方差的算术平方根。在数学意义上，代表的是一组数据离平均值的分散程度。
所以 np.var(b)=1.25, np.std(b)=1.118033988749895。
"""
print(np.std(b))
print(np.var(b))

"""
排序是算法中使用频率最高的一种，也是在数据分析工作中常用的方法，
计算机专业的同学会在大学期间的算法课中学习。

那么这些排序算法在 NumPy 中实现起来其实非常简单，一条语句就可以搞定。
这里你可以使用 sort 函数，
sort(a, axis=-1, kind=‘quicksort’, order=None)，
默认情况下使用的是快速排序；
在 kind 里，可以指定 quicksort、mergesort、heapsort
分别表示快速排序、合并排序、堆排序。
同样 axis 默认是 -1，即沿着数组的最后一个轴进行排序，
也可以取不同的 axis 轴，或者 axis=None 代表采用扁平化的方式作为一个向量进行排序。
另外 order 字段，对于结构化的数组可以指定按照某个字段进行排序。
"""
c = np.array([[4,3,2],[2,4,1]])
print(np.sort(c))
print(np.sort(c, axis=None))
print(np.sort(c, axis=0))
print(np.sort(c, axis=1))


# 多种创建数组的函数
my_new_array1 = np.zeros((2,3))
print(my_new_array1)
# [[0. 0. 0.]
#  [0. 0. 0.]]

my_new_array2 = np.ones((5))
print(my_new_array2)
#[1. 1. 1. 1. 1.]

my_new_array3 = np.full((2,2), 7)
print(my_new_array3)
# [[7 7]
#  [7 7]]

# 生成一个4x4的单位矩阵
my_identity_array = np.eye(4)
print(my_identity_array)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# 生出有5个随机数的一行
my_random_array = np.random.random((5))
print(my_random_array)
# [0.67142881 0.95339574 0.19678033 0.86407198 0.95639904]

# 截取my_identity_array中的第二列
my_array_column_2 = my_identity_array[:, 1]
print(my_array_column_2)
# [0. 1. 0. 0.]

# 矩阵的乘法
a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
matrix_product = a.dot(b)
print("Matrix Product = ",matrix_product)


# 数组中的元素会跟着一起变化
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[:2, 1:3]
# [[2 3]
#  [6 7]]
print(a[0, 1])
# 2
b[0, 0] = 77
print(a[0, 1])
# 77

# 不一样的切片效果
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
#横切
row_r1 = a[1, :]
row_r2 = a[1:2, :]
print(row_r1, row_r1.shape)
# [5 6 7 8] (4,)
print(row_r2, row_r2.shape)
# [[5 6 7 8]] (1, 4)

#竖切
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
# [ 2  6 10] (3,)
print(col_r2, col_r2.shape)
# [[ 2]
#  [ 6]
#  [10]] (3, 1)

# 整数数组索引的一个有用技巧是从矩阵的每一行中选择或改变一个元素：
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(a)
# [[ 1,  2,  3],
#  [ 4,  5,  6],
#  [ 7,  8,  9],
#  [10, 11, 12]]
b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b])
# [ 1  6  7 11]
a[np.arange(4), b] += 10
print(a)
# [[ 11, 2,  3],
#  [ 4,  5,  16],
#  [ 17, 8,  9],
#  [ 10, 21, 12]]

# 布尔数组索引: 布尔数组索引允许你选择数组的任意元素。
# 通常，这种类型的索引用于选择满足某些条件的数组元素。
a = np.array([[1,2], [3, 4], [5, 6]])
bool_idx = (a > 2)
print(bool_idx)
# [[False False]
#  [ True  True]
#  [ True  True]]
print(a[bool_idx])
# [3 4 5 6]
print(a[a > 2])
# [3 4 5 6]

# 矩阵的转置
# 要转置一个矩阵，只需使用一个数组对象的T属性：
x = np.array([[1,2], [3,4]])
print(x)
# [[1 2]
#  [3 4]]
print(x.T)
# [[1 3]
#  [2 4]]
v = np.array([1,2,3])
print(v)
# [1 2 3]
print(v.T)
# [1 2 3]

# 广播的使用
# 广播(Broadcasting)是一种强大的机制，它允许numpy在执行算术运算时使用不同形状的数组。
v = np.array([1,2,3])
w = np.array([4,5])
print(np.reshape(v, (3, 1)) * w)
# [[ 4  5]
#  [ 8 10]
#  [12 15]]
x = np.array([[1,2,3], [4,5,6]])
print(x + v)
# [[2 4 6]
#  [5 7 9]]
print((x.T + w).T)
print(x + np.reshape(w, (2, 1)))
# 以上两句等价
# [[ 5  6  7]
#  [ 9 10 11]]
print(x * 2)
# [[ 2  4  6]
#  [ 8 10 12]]