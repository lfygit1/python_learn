# 题目1：简单求和函数
# 需求：定义一个函数get_sum，接收两个数字参数a和b，返回这两个数的和。调用函数，传入参数10和25，打印结果。
# 思路：基础函数定义，def关键字+参数+return返回值，直接调用即可。
def get_sum(a, b):
    return a + b
# print(get_sum(10, 25))

# 题目2：带默认参数的问候函数
# 需求：定义一个函数greet，接收姓名（必选参数）和问候语（默认参数，默认值为"你好"），输出"问候语+姓名"。
# 调用1：只传姓名"小明"，使用默认问候语。
# 调用2：传姓名"小红"和问候语"早上好"，使用自定义问候语。
# 思路：默认参数放在必选参数后面，调用时可省略默认参数。
def greet(name, message="你好"):
    print(message + name)
# greet("小明")
# greet("小红", "早上好")

# 题目3：求列表平均值的函数
# 需求：定义一个函数get_average，接收一个数字列表作为参数，计算并返回列表的平均值。
# 测试：传入列表[80, 90, 75, 85]，打印平均值。
# 思路：用sum()求列表和，len()求列表长度
def get_average(lst):
    return sum(lst) / len(lst)
list1 = [80, 90, 75, 85]
# print(get_average(list1))

# 题目4：判断奇偶函数
# 需求：定义一个函数is_even，接收一个整数参数n，如果是偶数返回True，奇数返回False。
# 测试：分别传入17和24，打印结果。
# 思路：用取模运算%，n%2==0即为偶数。
def is_even(n):
    return n % 2 == 0
# print(is_even(17))

# 题目5：无返回值的打印函数
# 需求：定义一个函数print_info，接收任意多个字符串参数（可变参数*args），依次打印每个参数，每个参数占一行。
# 测试：传入"Python"，"函数"，"基础练习"，查看打印结果。
def print_info(*args):
    for i in args:
        print(i)
# print_info("Python", "函数", "基础练习")

# 题目6：基础类定义与实例化
# 需求：定义一个Dog类，包含实例属性：name（名字）、age（年龄）；包含实例方法：bark()，输出"名字+汪汪叫"。
# 创建Dog类的实例：名字"旺财"，年龄3。
# 打印实例的名字和年龄。
# 调用实例的bark()方法。
# 思路：__init__方法初始化实例属性，方法中通过self访问属性。
# 定义Dog类
class Dog:
    def __init__(self, name, age):
        # 初始化实例属性
        self.name = name
        self.age = age
    
    def bark(self):
        # 实例方法：输出名字+汪汪叫
        print(f"{self.name}汪汪叫")

# 创建实例
dog = Dog("旺财", 3)

# 打印实例属性
# print(dog.name)  # 输出：旺财
# print(dog.age)   # 输出：3

# # 调用实例方法
# dog.bark()       # 输出：旺财汪汪叫

# 题目7：简单购物类
# 需求：定义一个Shopping类，包含实例属性：total（总金额，初始值0）。
# 包含两个方法：
# add_goods：接收一个数字参数（商品价格），将价格加到total上。
# show_total：无参数，打印"当前购物车总金额：XXX元"。
# 测试：

# 创建Shopping实例。
# 依次添加商品：59元、129元、89元。
# 调用show_total查看总金额。
class Shopping:
    def __init__(self):
        self.total = 0
    
    def add_goods(self, price):
        self.total += price
    
    def show_total(self):
        print(f"当前购物车总金额：{self.total}元")
        return self.total
    
goods1=Shopping()
# goods1.add_goods(59)
# goods1.add_goods(129)
# goods1.add_goods(89)
# goods1.show_total()
# print(goods1.show_total())



# 题目8：函数调用类的方法
# 需求：定义一个Book类，包含属性name（书名）、price（价格），方法get_info返回"书名：XXX，价格：XXX元"。
# 定义一个函数print_book_info，接收一个Book类的实例作为参数，调用实例的get_info方法并打印结果。
# 测试：创建Book实例（书名"Python基础"，价格39.9），调用print_book_info函数。
class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_info(self):
        return f"书名：{self.name}，价格：{self.price}元"

def print_book_info(book):
    print(book.get_info())

book = Book("Python基础", 39.9)
print_book_info(book)
