"""类的继承"""


def __init__(self, style, color, age):
    self.style = style
    self.color = color
    self.age = age
    self.custmer_n = ''
    self.custmer_address = ''
    self.cust_tel = ''
class Friend():
    def __init__(self,name,age,high):
        self.name=name
        self.age=age
        self.high=high
    def eat(self,what):

        print(f'{self.age}岁，身高{self.high}的{self.name}喜欢吃{what}')

    def play(self,play):
        print(f'{self.age}岁，身高{self.high}的{self.name}喜欢玩{play}')

class GrilFriend(Friend):
    def __init__(self, name, age, high, sex,eat):
        super().__init__(name, age, high)
        self.sex = sex

    def sleep(self):
        print(f'号女生{self.name}今年{self.age}岁，身高{self.high},性别{self.sex}.整天除了吃{self.eat}就是{self.sleep}')


friend1=GrilFriend('王钢蛋', 19, 158, '女','垃圾食品')
friend1.sleep()

