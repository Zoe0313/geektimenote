"""
ORM（Object Relational Mapping，简称ORM）是Python对象与数据库关系表的一种映射关系，
有了ORM后，我们就不再需要写SQL语句，而可以直接使用Python的数据结构了。
ORM框架的优点，是提高了写代码的速度，同时兼容多种数据库系统，如SQLite、MySQL、PostgreSQL等这些数据库；
而付出的代价，可能就是性能上的一些损失。

peewee，正是其中一种基于Python的ORM框架，它的学习成本非常低，可以说是Python中最流行的ORM框架。
"""

import peewee
from peewee import *

db = MySQLDatabase('country', user='root', passwd='666888')


class Price(peewee.Model):
    timestamp = peewee.DateTimeField(primary_key=True)
    BTCUSD = peewee.FloatField()

    class Meta:
        database = db


def test_peewee():
    Price.create_table()
    price = Price(timestamp='2019-06-07 13:17:18', BTCUSD='12345.67')
    price.save()


test_peewee()
