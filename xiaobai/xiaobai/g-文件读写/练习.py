# 1、定义一个函数 calculate_area，接收圆的半径 r 作为参数，返回圆的面积（π 取 3.14159）；
# 调用该函数，分别计算半径为 5、8 的圆的面积并输出；
# 增加参数校验：如果半径≤0，返回提示字符串 "半径必须为正数"。
def calculate_area(r):
    if r <=0:
        return ('半径必须为正数')
    else:
        return 3.14159*r*r

# print(calculate_area(5))
# print(calculate_area(8))
# print(calculate_area(-8))

# 2、定义一个函数 calculate_sum，支持以下功能：
# 计算多个数字的和（可变参数 *args）；
# 可选参数 is_average（默认值 False），若为 True，返回平均值而非总和；
def calculate_sum(*args,is_average=False):
    totle=sum(args)
    if is_average:
        return totle/len(args)
    else:
        return totle

# print(calculate_sum(1,2,3,4,is_average=True))


# 3、定义一个 Person 类，包含：
# 实例属性：name（姓名）、age（年龄）；
# 实例方法：introduce()，输出 "我叫 XX，今年 XX 岁"；
# 创建 Person 类的实例（如：姓名 "张三"，年龄 20），调用 introduce() 方法；
# 给类增加一个类属性 species = "人类"，并输出该属性。

# 4、基于题目 3的 Person 类，定义子类 Student，新增：
# 实例属性：student_id（学号）、score（成绩）；
# 重写 introduce() 方法，输出 "我叫 XX，学号 XX，成绩 XX 分"；
# 新增实例方法：get_grade()，根据成绩返回等级（≥90：A，≥80：B，≥60：C，<60：D）；
# 创建 Student 实例（姓名 "李四"，年龄 18，学号 "2024001"，成绩 85），调用 introduce() 和 get_grade()。
class Person():
    species = "人类"
    def __init__(self,name,age,):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'我叫{self.name},今年{self.age}')
class Student(Person):  # 创建子类Student,继承父类
    def __init__(self,name,age,student_id,score):
        super().__init__(name,age)
        self.student_id=student_id
        self.score =score
    def introduce(self):
        return (f'我叫{self.name},学号{self.student_id},成绩{self.score}')
    def get_grade(self):
        if self.score>=90:
            return '牛逼，给你A'
        elif self.score>=80:
            return '一般，给你B'
        elif self.score>=60:
            return '不行，给个C'
        else:
            return '你学了个蛋啊，拿个D滚犊子'

# person1=Person('张三',20)
# person1.introduce()
# print(Person.species)
#
# person2=Student('李四',20,20250011,20)
# print(Student.introduce(person2))
# print(Student.get_grade(person2))





# 5、定义一个 ShoppingCart 类，实现购物车功能：
# 实例属性：items（列表，存储商品字典，格式：{"name": 商品名，"price": 价格，"quantity": 数量}）；
# 方法 add_item(name, price, quantity=1)：添加商品（价格 > 0、数量≥1 才生效，否则提示错误）；
# 方法 remove_item(name)：删除指定名称的商品（不存在则提示）；
# 方法 calculate_total()：计算购物车总金额，返回数值；
# 方法 show_cart()：打印购物车所有商品和总金额；
import json

# items.pop(1)
# print(items)
class ShoppingCart():
    def __init__(self):
        self.items=[]
    def add_items(self,name,price,quantity):
        if price>0 :
            if quantity>=1:
                d = {"name": name, "price": price, "quantity": quantity}
                self.items.append(d)
            else:
                print('数量必须大于一')
        else:
            print('价格必须大于0')
    def remove_item(self,name):
        k=[]
        for i in self.items:
            k.append(i["name"])
        if name in k:
            for i in self.items:
                if i["name"]==name:
                    self.items.remove(i)
                    return '删除成功'
        else:
            print('要删除的商品不存在')
    def calculate_total(self):
        s=0
        for i in self.items:
            s= s+ i["price"]*i["quantity"]
            print(f'{i["name"]}的价格是{i["price"]}，你买了{i["quantity"]}个，总计{s}元')


    def show_cart(self):
        k=[]
        for i in self.items:
            k.append(i["name"])
        print(k)
        print(self.calculate_total())
items=[{"name":"辣条","price":1,"quantity":3},
       {"name":"鸡爪","price":5,"quantity":4}]

p1=ShoppingCart()
p1.add_items('鸡腿',10,2)
print(p1.items)
p1.remove_item('鸡肉')
print(p1.items)
p1.calculate_total()
p1.show_cart()