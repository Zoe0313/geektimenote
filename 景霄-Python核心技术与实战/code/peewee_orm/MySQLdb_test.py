"""
数据库有了量化数据存入后，接下来，我们便可以开始进行一些量化分析了。
这一块儿也是一个很大的学术领域，叫做时间序列分析，不过就今天这节课的主题来说，我们仅做抛砖引玉.
列举一个非常简单的例子，即求过去一个小时BTC/USD的最高价和最低价。
"""

import MySQLdb
import numpy as np


def test_pymysql():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='666888',
        db='country'
    )

    cur = conn.cursor()
    cur.execute('''
            SELECT
              BTCUSD
            FROM
              price
            WHERE
              timestamp > now() - interval 60 minute
    ''')

    BTCUSD = np.array(cur.fetchall())
    print(BTCUSD.max(), BTCUSD.min())

    conn.close()


test_pymysql()
