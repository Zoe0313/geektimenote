"""
假设一个团队里有 5 名学员，成绩如下表所示。
你可以用 NumPy 统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
然后把这些人的总成绩排序，得出名次进行成绩输出。

姓名   语文   英语   数学
张飞   66     65    30
关羽   95     85    98
赵云   93     92    96
黄忠   90     88    77
典韦   80     90    90
"""

import numpy as np

stu_type = np.dtype({
    'names': ['name', 'chinese', 'english', 'math'],
    'formats': ['S32', 'i', 'i', 'i']
})

stu_array = np.array(
    [
        ('zhangfei', 66, 65, 30),
        ('guanyu', 95, 85, 98),
        ('zhaoyun', 93, 92, 96),
        ('huangzhong', 90, 88, 77),
        ('dianwei', 80, 90, 90)
    ],
    dtype=stu_type
)

stu = stu_array[:]

chinese_score = stu['chinese']
english_score = stu['english']
math_score = stu['math']
print('平均成绩: 语文%s 英语%s 数学%s'%(np.mean(chinese_score),np.mean(english_score),np.mean(math_score)))
print('最小成绩: 语文%s 英语%s 数学%s'%(np.min(chinese_score),np.min(english_score),np.min(math_score)))
print('最大成绩: 语文%s 英语%s 数学%s'%(np.max(chinese_score),np.max(english_score),np.max(math_score)))
print('方差: 语文%s 英语%s 数学%s'%(np.var(chinese_score),np.var(english_score),np.var(math_score)))
print('标准差: 语文%s 英语%s 数学%s'%(np.std(chinese_score),np.std(english_score),np.std(math_score)))

print('排名:')
rank = sorted(stu, key=lambda s:s[1]+s[2]+s[3], reverse=True)
print(rank)


