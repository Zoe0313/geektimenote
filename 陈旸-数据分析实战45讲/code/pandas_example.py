"""
在数据分析工作中，Pandas 的使用频率是很高的，
一方面是因为 Pandas 提供的基础数据结构 DataFrame 与 json 的契合度很高，转换起来就很方便。
另一方面，如果我们日常的数据清理工作不是很复杂的话，你通常用几句 Pandas 代码就可以对数据进行规整。

Pandas 可以说是基于 NumPy 构建的含有更高级数据结构和分析能力的工具包。
在 NumPy 中数据结构是围绕 ndarray 展开的，那么在 Pandas 中的核心数据结构是什么呢？

下面主要给你讲下Series 和 DataFrame 这两个核心数据结构，
他们分别代表着一维的序列和二维的表结构。
基于这两种数据结构，Pandas 可以对数据进行导入、清洗、处理、统计和输出。

数据结构：Series 和 DataFrame
Series 是个定长的字典序列。
说是定长是因为在存储的时候，相当于两个 ndarray，这也是和字典结构最大的不同。
因为在字典的结构里，元素的个数是不固定的。

Series有两个基本属性：index 和 values。
在 Series 结构中，index 默认是 0,1,2,……递增的整数序列，
当然我们也可以自己来指定索引，比如 index=[‘a’, ‘b’, ‘c’, ‘d’]。
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
x1 = Series([1,2,3,4])
x2 = Series(data=[1,2,3,4], index=['a', 'b', 'c', 'd'])
print(x1)
print(x2)


"""
DataFrame 类型数据结构类似数据库表。
它包括了行索引和列索引，我们可以将 DataFrame 看成是由相同索引的 Series 组成的字典类型。
我们虚构一个王者荣耀考试的场景，想要输出几位英雄的考试成绩：
"""
data = {'Chinese': [66, 95, 93, 90,80],
        'English': [65, 85, 92, 88, 90],
        'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data,
                index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])
print(df1)
print(df2)
"""
df2:
            English  Math  Chinese
ZhangFei         65    30       66
GuanYu           85    98       95
ZhaoYun          92    96       93
HuangZhong       88    77       90
DianWei          90    90       80
"""

"""
Pandas 允许直接从 xlsx，csv 等文件中导入数据，也可以输出到 xlsx, csv 等文件，非常方便。
此过程需要用到xlrd 和 openpyxl两个包
"""
score = DataFrame(pd.read_excel('data.xlsx'))
score.to_excel('data1.xlsx')
print(score)

"""
简单介绍Pandas在数据清洗中的简单用法：
"""
data = {'Chinese': [66, 95, 93, 90, 80, 80],
        'English': [65, 85, 92, 88, 90, 90],
        'Math': [30, 98, 96, 77, 90, 90]}
df2 = DataFrame(data,
                index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])

#删除DataFrame中的列：
df2 = df2.drop(columns=['Chinese'])
print(df2)

#删除DataFrame中的行：
df2 = df2.drop(index=['ZhangFei'])
print(df2)

#重命名列名columns
df2.rename(columns={'Math':'Shuxue','English':'yingyu'},inplace=True)
print(df2)

#去除重复的行
df2 = df2.drop_duplicates()
print(df2)

# # 格式问题
# # 1.更改数据格式
# df2['Chinese'].astype('str')
# df2['Chinese'].astype(np.int64)
#
# # 2.数据间的空格
# # 删除左右两边空格
# df2['Chinese']=df2['Chinese'].map(str.strip)
# # 删除左边空格
# df2['Chinese']=df2['Chinese'].map(str.lstrip)
# # 删除右边空格
# df2['Chinese']=df2['Chinese'].map(str.rstrip)
#
# df2['Chinese']=df2['Chinese'].str.strip('$')
#
# # 3.大小写转换
# # 全部大写
# df2.columns = df2.columns.str.upper()
# # 全部小写
# df2.columns = df2.columns.str.lower()
# # 首字母大写
# df2.columns = df2.columns.str.title()

# 4.查找空值
# 如果我们想看下哪个地方存在空值 NaN，可以针对数据表 df 进行 df.isnull()
# 如果我想知道哪列存在空值，可以使用 df.isnull().any()

"""
统计大礼包describle()函数可以快速让我们对数据有个全面的了解
"""
df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
print(df1)
print(df1.describe())
"""
       name  data1
0  ZhangFei      0
1    GuanYu      1
2         a      2
3         b      3
4         c      4

          data1
count  5.000000
mean   2.000000
std    1.581139
min    0.000000
25%    1.000000
50%    2.000000
75%    3.000000
max    4.000000
"""


#在 Python 里可以直接使用 SQL 语句来操作 Pandas。
import pandas as pd
from pandas import DataFrame
from pandasql import sqldf, load_meat, load_births
df1 = DataFrame({'name':['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1':range(5)})
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name ='ZhangFei'"
print(pysqldf(sql))
















