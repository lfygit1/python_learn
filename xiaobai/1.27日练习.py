# 3、可变参数求和
# 编写函数 sum_all(*numbers)，接受任意数量的数字参数，返回它们的总和（例如 sum_all(1,2,3) 返回 6）。
# def sum_all(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# print(sum_all(1,2,3))
# 4、判断奇偶性
# 编写函数 is_even(num)，如果数字是偶数返回 True，否则返回 False。
# def is_even(num):
#     return num % 2 == 0
# print(is_even(9))
# 5、反转字符串
# 编写函数 reverse_string(s)，返回输入字符串的逆序（如输入 "hello" 返回 "olleh"）。
# s='hello'
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string(s))
# 6、统计元音字母
# 编写函数 count_vowels(s)，统计字符串中元音字母 (a, e, i, o, u) 的数量，不区分大小写。
# s='jdklfjjoierorpoewrurOEWUROIW'
# def count_vowels(s):
#     count = 0
#     for char in s:
#         if char.lower() in 'aeiou':
#             count += 1
#     return count
# print(count_vowels(s))
# 7、检查回文字符串
# 编写函数 is_palindrome(s)，判断字符串是否是回文（正读反读相同）。
# s='jdklfjjoierorpoewrurOEWUROIW'
# def is_palindrome(s):
#     return s == s[::-1]
# print(is_palindrome(s))
# 8、查找列表最大值
# 编写函数 find_min_max(lst)，返回列表中最大值（如输入 [3, 1, 4] 返回 4）。
# s=[3, 1, 4]
# def find_min_max(lst):
#     return max(lst)
# print(find_min_max(s))
# 9、合并并去重列表
# 编写函数 merge_unique(list1, list2)，合并两个列表并去除重复元素（如输入 [1,2] 和 [2,3]，返回 [1,2,3]）。
# lst1=[1,2]
# lst2=[2,3]
# def merge_unique(list1, list2):
#     list2.extend(lst1)
#     return list(set(list2))
# print(merge_unique(lst1, lst2))
# 10、计算列表平均值
# 编写函数 average(lst)，计算列表中数字的平均值。
# s=[1,2,3,4]
# def average(lst):
#     return sum(lst) / len(lst)
# print(average(s))
# 11、筛选偶数
# 编写函数 filter_even(lst)，返回列表中所有偶数的列表（如输入 [1,2,3,4] 返回 [2,4]）。
# def filter_even(lst):
#     ls=[]
#     for i in lst:
#         if i % 2 ==0:
#             ls.append(i)
#     return ls
# s=[1,2,3,4]
# print(filter_even(s))

# 【练习题 1：定义一个学生类】
# 考察点：类的定义、__init__方法，实例属性，实例方法
# 要求：类包含 姓名(name)/年龄(age)/学号(student_id)三个实例属性
# 定义一个show_info()方法， 打印学生信息（格式：姓名：XX，年龄：XX，学号：XX）
# 定义一个 update_age()方法 修改学生年龄
# 创建实例并调用测试方法
# class Student:
#     def __init__(self,name,age,student_id):
#         self.name = name
#         self.age = age
#         self.student_id = student_id
#     def show_info(self):
#         print(f'姓名:{self.name},年龄：{self.age},学号：{self.student_id}')
#     def update_age(self,new_age):
#         self.age = new_age
#         print(f'姓名{self.name},年龄已更新为:{new_age}')
# stu1=Student('张三',18,'20210001')
# stu1.show_info()
# stu1.update_age(19)
# stu1.show_info()

# 【练习题 2：计算器类】
# 考察点：实例方法，参数传递，简单逻辑实现
# 要求：类无需初始化属性，定义4个实例方法：add()/sub()/mul()/div()  （加减乘除）每个方法接收两个数字参数，返回计算结果
# 创建实例并调用每个方法测试（示例：add(10,5) 返回 15）
# class Calculator:
#     def add(self,num1,num2):
#         return num1 + num2
#     def sub(self,num1,num2):
#         return num1 - num2
#     def mul(self,num1,num2):
#         return num1 * num2
#     def div(self,num1,num2):
#         return num1 / num2

# res=Calculator()
# print(res.add(10,5))
# print(res.sub(10,5))
# print(res.mul(10,5))
# print(res.div(10,5))

# class Calculator:
#     def add(self, numbers):      # 修改为接收一个列表参数
#         return numbers[0] + numbers[1]  # 从列表中取元素相加
    
#     def sub(self, numbers):      # 同样修改其他方法
#         return numbers[0] - numbers[1]
    
#     def mul(self, numbers):
#         return numbers[0] * numbers[1]
    
#     def div(self, numbers):
#         return numbers[0] / numbers[1]

# # 使用方式
# res = Calculator()
# s = [10, 5]                    # 定义包含两个数字的列表
# print(res.add(s))              # 传入列表 s，输出 15
# print(res.sub(s))              # 传入列表 s，输出 5
# print(res.mul(s))              # 传入列表 s，输出 50
# print(res.div(s))              # 传入列表 s，输出 2.0


# 练习题3：图书管理系统（简易版）
# 考察点：类的组合、实例列表、综合逻辑实现
# 要求：
# 定义「图书类（Book）」：
# 初始化属性：book_id（图书编号）、title（书名）、author（作者）、status（状态：默认「未借出」）；
# 定义borrow()方法：若状态为「未借出」，则改为「已借出」，返回「借阅成功」；否则返回「该书已借出」；
# 定义return_book()方法：若状态为「已借出」，则改为「未借出」，返回「归还成功」；否则返回「该书未借出」。
# class Book():
#     def __init__(self, book_id, title, author, status='未借出'):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.status = status

#     def borrow(self):
#         if self.status == '未借出':
#             self.status = '已借出'
#             return '借阅成功'
#         else:
#             return '该书已借出'
#     def return_book(self):
#         if self.status == '已借出':
#             self.status = '未借出'
#             return '归还成功'
#         else:
#             return '该书未借出'
# book1 = Book('001', '《Python基础》', '张三')
# print(book1.borrow())
# print(book1.return_book())



# 定义「图书馆类（Library）」：
# 初始化属性：books（空列表，存储图书实例）；
# 定义add_book()方法，接收图书实例，添加到列表；
# 定义find_book()方法，接收书名，返回匹配的图书实例（无则返回None）；
# 定义show_all_books()方法，打印所有图书的信息（编号、书名、作者、状态）。
# 测试流程：
# 创建3本图书实例，添加到图书馆；
# 打印所有图书信息，验证状态是否正确。
class Book:
    def __init__(self, book_id, title, author, status='在馆'):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
    
    def __str__(self):
        return f"编号: {self.book_id}, 书名: {self.title}, 作者: {self.author}, 状态: {self.status}"


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        """添加图书到图书馆"""
        self.books.append(book)
    
    def find_book(self, title):
        """根据书名查找图书（不区分大小写）"""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def show_all_books(self):
        """打印所有图书信息"""
        if not self.books:
            print("图书馆暂无图书")
            return
        print("图书馆所有图书信息：")
        for book in self.books:
            print(book)


# 测试流程
if __name__ == "__main__":
    # 创建图书馆实例
    library = Library()
    
    # 创建3本图书实例
    book1 = Book(1, "Python编程", "张三", "在馆")
    book2 = Book(2, "算法导论", "李四", "在馆")
    book3 = Book(3, "数据结构", "王五", "借出")
    
    # 添加图书到图书馆
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # 打印所有图书信息
    library.show_all_books()
    
    # 测试查找图书功能
    # print("\n测试查找图书：")
    # found_book = library.find_book("python编程")
    # if found_book:
    #     print(f"找到图书: {found_book}")
    # else:
    #     print("未找到图书")
    
    # found_book = library.find_book("不存在的书")
    # if found_book:
    #     print(f"找到图书: {found_book}")
    # else:
    #     print("未找到图书")

# 1、定义一个函数 calculate_area,接收圆的半径作为参数，返回圆的面积(取3.14159);  
#调用该函数，分别计算半径为5、8的圆的面积并输出；  
#增加参数校验:如果半径≤0,返回提示字符串"半径必须为正数"。 
def calculate_area(radius):
    if radius <= 0:
        return "半径必须为正数"
    else:
        return 3.14159 * 2 ** 2
# print(calculate_area(8))





#2、定义一个函数calculate_sum,支持以下功能: 
#计算多个数字的和(可变参数*args); 
#可选参数is_ average (默认值False),若为True，返回平均值而非总和； 
def calculate_sum(*args, is_average=False):
    total = sum(args)
    if is_average:
        return total / len(args)
    else:
        return total

print(calculate_sum(1,2,3,4,5,is_average=True))


#3、定义一个Person类，包含: 
#实例属性:name (姓名)、age (年龄) 
#实例方法:introduce0.输出"我叫XX，今年XX岁"； 
#创建Person类的实例(如:姓名"张三·，年龄20),调用introduce0方法； 
#给类增加个类属性species-"人类”，并输出该属性。 

#4、基于题目3的Person类，定义子类Student，新增: 
#实例属性:studentid(学号)、score (成绩)；
#重写introduce0方法，输出"我叫 XX,学号XX，成绩X分； 
#新增实例方法:get grade0,根据成绩返回等级(>90:A,≥80:B,≥60:C,<60:D); 
#创建Student实例(姓名"李四"，年龄18，学号"2024001",成绩85),调用introduce0和get_grade0。
class Person:
    species = "人类"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁")

class Student(Person):
    def __init__(self, name, age, studentid, score):
        super().__init__(name, age)
        self.studentid = studentid
        self.score = score
    def introduce(self):
        print(f"我叫{self.name}，学号{self.studentid}，成绩{self.score}分")
    def get_grade(self):
        if self.score > 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 60:
            return "C"
        else:
            return "D"
stu1=Student("李四",18,"2024001",85)
# stu1.introduce()
# print(stu1.get_grade())

    






#5、定义一个ShoppingCart类，实现购物车功能: 
#实例属性: items (列表，存储商品字典，格式:(Cname":商品名，"price:价格，"quantity':数量)):  
#方法add item(name,price.quantity=1):添加商品(价格>0、数量≥1才生效，否则提示错误)； 
#方法remove_item(name):删除指定名称的商品(不存在则提示)； 
#方法calculate_total:计算购物车总金额，返回数值； 
#方法show_cart:打印购物车所有商品和总金额；
class ShoppingCart():
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        if price <= 0 or quantity < 1:
            print("价格必须大于0，数量必须大于等于1")
        else:
            item = {"name": name, "price": price, "quantity": quantity}
            self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return
        return "未找到该商品"
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        return total
    def show_cart(self):
        total = self.calculate_total()
        print("购物车中的商品:")
        for item in self.items:
            print(f"商品名:{item['name']},价格:{item['price']},数量:{item['quantity']}")
        return(f"总金额:{total}")
f=ShoppingCart()
f.add_item("手机", 5000, 2)
f.add_item("电脑", 10000, 1)

f.show_cart()

f.remove_item("手机")
f.show_cart()
print(f.calculate_total())
print(f.remove_item("电脑"))
f.show_cart()

