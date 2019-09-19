import matplotlib.pyplot as plt
import pandas as pd
import requests

# 选择要获取的数据时间段
periods = '3600'

# 通过 Http 抓取 btc 历史价格数据
# https://api.cryptowat.ch/markets/gemini/btcusd/ohlc?periods=3600
resp = requests.get('https://api.cryptowat.ch/markets/gemini/btcusd/ohlc', 
  params={
    'periods': periods
  })
data = resp.json()

# 转换成 pandas data frame
df = pd.DataFrame(
  data['result'][periods], 
  columns=[
    'CloseTime',
    'OpenPrice',
    'HighPrice',
    'LowPrice',
    'ClosePrice',
    'Volume',
    'NA'])

# 输出 DataFrame 的头部几行
print(df.head())

# 绘制 btc 价格曲线
df['ClosePrice'].plot(figsize=(14, 7))
plt.show()

########### 输出 ###############
#     CloseTime  OpenPrice  HighPrice  ...  ClosePrice     Volume             NA
# 0  1562410800   11448.95   11464.34  ...    11388.95   8.630603   98693.705273
# 1  1562414400   11383.92   11421.50  ...    11421.50  15.143432  172187.970847
# 2  1562418000   11437.01   11524.34  ...    11451.96  62.760156  719935.318685
# 3  1562421600   11454.51   11465.07  ...    11395.87  17.552419  200417.444371
# 4  1562425200   11395.87   11438.05  ...    11432.66   9.424474  107553.914421
#
# [5 rows x 7 columns]