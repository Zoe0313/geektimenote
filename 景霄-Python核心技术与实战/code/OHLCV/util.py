from os import path
import pandas as pd


def assert_msg(condition, msg):
    if not condition:
        raise Exception(msg)


def read_file(filename):
    # 获得文件绝对路径
    filepath = path.join(path.dirname(__file__), filename)
    print(__file__)

    # 判定文件是否存在
    assert_msg(path.exists(filepath), " 文件不存在 ")

    # 读取 CSV 文件并返回
    return pd.read_csv(filepath,
                       index_col=0,
                       parse_dates=True,
                       infer_datetime_format=True)

def SMA(values, n):
    """
    返回简单滑动平均
    """
    return pd.Series(values).rolling(n).mean()

def crossover(series1, series2) -> bool:
    """
    检查两个序列是否在结尾交叉
    :param series1:  序列 1
    :param series2:  序列 2
    :return:         如果交叉返回 True，反之 False
    """
    return series1[-2] < series2[-2] and series1[-1] > series2[-1]


# BTCUSD = read_file('BTCUSD_GEMINI.csv')
# assert_msg(BTCUSD.__len__() > 0, '读取失败')
# print(BTCUSD.head())

########## 输出 ##########
# Time                 Symbol      Open      High       Low     Close     Volume
# Date
# 2019-07-08 00:00:00  BTCUSD  11475.07  11540.33  11469.53  11506.43  10.770731
# 2019-07-07 23:00:00  BTCUSD  11423.00  11482.72  11423.00  11475.07  32.996559
# 2019-07-07 22:00:00  BTCUSD  11526.25  11572.74  11333.59  11423.00  48.937730
# 2019-07-07 21:00:00  BTCUSD  11515.80  11562.65  11478.20  11526.25  25.323908
# 2019-07-07 20:00:00  BTCUSD  11547.98  11624.88  11423.94  11515.80  63.211972
