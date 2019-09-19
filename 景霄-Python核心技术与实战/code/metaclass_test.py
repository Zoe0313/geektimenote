import yaml

yaml_str = """
name: 灰蓝
age: 0
job: Tester
"""

y = yaml.load(yaml_str)
print(y)
#{'name': '灰蓝', 'age': 0, 'job': 'Tester'}

python_obj = {"name": u"灰蓝",
              "age": 0,
              "job": "Tester"
              }

y = yaml.dump(python_obj, default_flow_style=False)
print(y)
"""
age: 0
job: Tester
name: "\u7070\u84DD"
"""


class Person(yaml.YAMLObject):
    yaml_tag = '!person'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '%s(name=%s, age=%d)' % (self.__class__.__name__, self.name, self.age)

james = Person('James', 20)
print(yaml.dump(james))  # Python对象实例转为yaml
#!person {age: 20, name: James}

lily = yaml.load('!person {name: Lily, age: 19}')
print(lily)  # yaml转为Python对象实例
#Person(name=Lily, age=19)


class Monster(yaml.YAMLObject):
  yaml_tag = u'!Monster'
  def __init__(self, name, hp, ac, attacks):
    self.name = name
    self.hp = hp
    self.ac = ac
    self.attacks = attacks
  def __repr__(self):
    return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
       self.__class__.__name__, self.name, self.hp, self.ac,
       self.attacks)

yaml.load("""
!Monster
ac: 16
attacks:
- BITE
- HURT
hp:
- 2
- 6
name: Cave spider
""")

#Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])

print(
	yaml.dump(Monster(
    name='Cave lizard',
    hp=[3,6],
    ac=16,
    attacks=['BITE','HURT']))
    )

"""
!Monster
ac: 16
attacks: [BITE, HURT]
hp: [3, 6]
name: Cave lizard
"""