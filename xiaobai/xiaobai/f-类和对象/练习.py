# 3、可变参数求和
# 编写函数 sum_all(*numbers)，接受任意数量的数字参数，返回它们的总和（例如 sum_all(1,2,3) 返回 6）。
def sum_all(*numbers):
    return sum(numbers)
num_list=[11,2]
# print(sum_all(*num_list))



# 4、判断奇偶性
# 编写函数 is_even(num)，如果数字是偶数返回 True，否则返回 False。
# def is_evev(num):
#     return num%2==0
# print(is_evev(9))


# 5、反转字符串
# 编写函数 reverse_string(s)，返回输入字符串的逆序（如输入 "hello" 返回 "olleh"）。
# s='hello'
#
# def reverse_string(s):
#     return (s[::-1])
# print(reverse_string(s))


# 6、统计元音字母
# 编写函数 count_vowels(s)，统计字符串中元音字母（a, e, i, o, u）的数量，不区分大小写。  统一转成大写或者小写
def count_vowels(s):
    c=0
    v={'a', 'e', 'i', 'o', 'u'}
    for i in s.lower():
        if i in v:
            c+=1
    return c
s='kldfdsfoisDOUADFQD'
# print(count_vowels(s))

# 7、检查回文字符串
# 编写函数 is_palindrome(s)，判断字符串是否是回文（正读反读相同）
def is_palindrome(s):
    return s==s[::-1]
s='dskfdfoiwaeofdkjf'
s1='asdsa'
# print(is_palindrome(s1))



# 8、查找列表最大值
# 编写函数 find_min_max(lst)，返回列表中最大值（如输入 [3, 1, 4] 返回4）。
# k=[65,45,40,35]
# def find_min_max(lst):
#     return max(k)
# print(find_min_max(k))

# 9、合并并去重列表
# 编写函数 merge_unique(list1, list2)，合并两个列表并去除重复元素（如输入 [1,2] 和 [2,3]，返回 [1,2,3]）。
# def merge_unique(list1, list2):
#     list2.extend(list1)
#     return set(list2)
# list1=[1,2,4,56,15]
# list2=[2,3,56,16,7]
# print(merge_unique(list1,list2))

def merge_unique(list1, list2):
    s=list1+list2
    return set(s)
list1=[1,2,4,56,15]
list2=[2,3,56,16,7]
# print(merge_unique(list1,list2))


# 10、计算列表平均值
# 编写函数 average(lst)，计算列表中数字的平均值。
list1=[4,34,543,5535,443,5]
def average(lst):
    return sum(lst)/len(lst)
# print(average(list1))

# 11、筛选偶数
# 编写函数 filter_even(lst)，返回列表中所有偶数的列表（如输入 [1,2,3,4] 返回 [2,4]）。
list1=[13,54,44,84,4843]
#
def filter_even(lst):
    list2 = []
    for i in lst:
        if i%2==0:
            list2.append(i)
    return list2
# print(filter_even(list1))

#
# 练习题 1：定义一个「学生类（Student）」
class Student():
    def __init__(self,name,age,student_id):
        self.name=name
        self.age=age
        self.student_id=student_id
    def show_info(self):
        print (f'姓名：{self.name},年龄：{self.age},学号：{self.student_id}')
    def update_age(self,new_age):
        self.age=new_age
        print(f'年龄已修改为{self.age}')
# stu1=Student('张三',18,20250101)
# stu1.show_info()
# stu1.update_age(20)
# stu1.show_info()


# 考察点：类的定义、__init__ 初始化方法、实例属性、实例方法
# 要求：
# 类包含「姓名（name）」「年龄（age）」「学号（student_id）」三个实例属性；
# 定义一个 show_info() 方法，打印学生的所有信息（格式：姓名：XX，年龄：XX，学号：XX）；
# 定义一个 update_age() 方法，接收一个参数，修改学生的年龄；
# 创建1个学生实例，调用上述方法测试。
#
#
# 练习题 2：定义一个「计算器类（Calculator）」
class Calculator():

    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return '除数不能为0'
        return a/b
    def jisuan(self,a,b):
        print(f'计算结果是{self.add}')
# re1=Calculator()
# print(f'a+b的值是{re1.add(10,2)}')
# print(f'a-b的值是{re1.sub(10,2)}')
# print(f'a*b的值是{re1.mul(10,2)}')
# print(f'a/b的值是{re1.div(10,2)}')
# 考察点：实例方法、参数传递、简单逻辑实现
# 要求：
# 类无需初始化属性，定义 4 个实例方法：add()（加法）、sub()（减法）、mul()（乘法）、div()（除法）；
# 每个方法接收两个数字参数，返回计算结果；
# 创建计算器实例，调用每个方法测试（如 add(10,5) 返回 15）。
#
# 练习题 3：图书管理系统（简易版）
# 考察点：类的组合、实例列表、综合逻辑实现
# 要求：
# 定义「图书类（Book）」：
class Book():
    def __init__(self,book_id,title,author,status='未借出'):
        self.book_id = book_id
        self.title=title
        self.author=author
        self.status=status
    def borrow(self):
        if self.status=='未借出':
            self.status='已借出'
            return '借阅成功'
        else:
            return '该书已借出'

    def return_book(self):
        if self.status=='已借出':
            self.status='未借出'
            return '归还成功'
        else:
            return '该书未借出'
# book1=Book('001','老人与海','海明威')
# book2=Book('002','Python基础','不知道是谁','已借出')
# book1.return_book()
# print(f'你想还的书是 {book1.title} 我给你瞅瞅 {book1.return_book()} OK，还书成功')
# book2.borrow()
# print((f'你想借的书是 {book2.title} 我给你瞅瞅 {book2.borrow()} 你走吧'))

# 初始化属性：book_id（图书编号）、title（书名）、author（作者）、status（状态：默认「未借出」）；
# 定义 borrow() 方法：若状态为「未借出」，则改为「已借出」，返回「借阅成功」；否则返回「该书已借出」；
# 定义 return_book() 方法：若状态为「已借出」，则改为「未借出」，返回「归还成功」；否则返回「该书未借出」。


# 定义「图书馆类（Library）」：
# 初始化属性：books（空列表，存储图书实例）；
# 定义 add_book() 方法，接收图书实例，添加到列表；
# 定义 find_book() 方法，接收书名，返回匹配的图书实例（无则返回 None）；
# 定义 show_all_books() 方法，打印所有图书的信息（编号、书名、作者、状态）。
# 测试流程：
# 创建 3 本图书实例，添加到图书馆；
# 打印所有图书信息，验证状态是否正确。
class Library():
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def show_all_books(self):
        bks=self.books
        for i in bks:
            print(f'编号:{i.book_id},书名：{i.title},作者：{i.author},状态：{i.status}')
    def find_book(self,sm):
        a=None
        for i in self.books:
            if i.title==sm:
                a = i
                return a

book1=Book('001','老人与海','海明威')
book2=Book('002','Python基础','不知道是谁')
book3=Book('003','Python进阶','爱谁谁')

L1=Library()
L1.add_book(book3)
L1.add_book(book2)
L1.add_book(book1)

# print(L1.show_all_books())
print(L1.find_book('Python进阶'))


