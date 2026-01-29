"""
类：一类相似事物的总称，模糊且不具体的概念
对象（实例）：具体到个体的
类的组成：类名、属性、方法
类的定义：遵循大驼峰命名，每个单词的首字母大写
class 类名():
    def __init__(self):
        属性
        行为

return 代表一个模块的结束，它后面的代码是不运行的
"""
class Friend():
    def __init__(self,name,age,high):
        self.name=name
        self.age=age
        self.high=high
    def eat(self,what):

        print(f'{self.age}岁，身高{self.high}的{self.name}喜欢吃{what}')

    def play(self,play):
        print(f'{self.age}岁，身高{self.high}的{self.name}喜欢玩{play}')

    def like(self,like):
        print(f'{self.age}岁，身高{self.high}的{self.name},闲着没事喜欢{like}')
# 魔术方法
# def __str__(self):
#     return f'{self.name}'
#
# def __gt__(self, other):
#     return self.age>other.age
#
# def __eq__(self, other):
#     return self.age ==other.age
#
# def __lt__(self, other):
#     return self.age<other.age
"""创建对象"""
"""对象=类名（实参）"""
"""调用属性或行为：对象.属性/行为"""


# f1=Friend('xioabai',18,178)
# f2=Friend('xiaohei',20,170)
# f3=Friend('xiaohuang',88,185)
# print(f1)
# f1.eat('馒头')
# f2.play('蹦极')
# f3.like('撸猫')

class Cat():
    def __init__(self, style, color, age):
        self.style = style
        self.color = color
        self.age = age
        self.custmer_n = ''
        self.custmer_address = ''
        self.cust_tel = ''

    def custmer_name(self, name):
        self.custmer_n = name
        # print(f'顾客姓名：{name}')

    def address(self, cust_address):
        self.custmer_address = cust_address
        # print(f'来自{cust_address}')

    def number(self, telphone):
        self.cust_tel = telphone

    def want(self):
        print(
            f'来自{self.custmer_address}的{self.custmer_n}先生，想要一只{self.color}的{self.age}大的{self.style}.他的联系方式是：{self.cust_tel}')


buyer1 = Cat('狸花猫', '黄色', '5个月')
buyer1.custmer_name('张三')
buyer1.address('北京')
buyer1.number('123546545135')
buyer1.want()

buyer2 = Cat('橘猫', '黄色', '9个月')
buyer2.custmer_name('赵老四')
buyer2.number('没留手机号，爱买不买吧')
buyer2.address('东北')
buyer2.want()








































