import math

x = "全局"


def outer():
    x = "外层"

    def inner_local():
        x = "局部"  # 新建局部变量

    def inner_nonlocal():
        nonlocal x  # 引用外层的 x
        x = "被nonlocal修改"

    def inner_global():
        global x  # 引用全局的 x
        x = "被global修改"

    inner_local()
    print(f"local后: {x}")  # 外层（没变）

    inner_nonlocal()
    print(f"nonlocal后: {x}")  # 被nonlocal修改

    inner_global()
    print(f"global后: {x}")  # 外层（没变）


outer()
print(f"全局: {x}")  # 被global修改

# 定义一个 `Rectangle` 类：
#
# 1. 有 `width` 和 `height` 属性
# 2. 有 `area()` 方法返回面积
# 3. 有 `perimeter()` 方法返回周长
# 4. 创建两个矩形对象并计算面积
def p1():
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2*self.width + 2*self.height

    a1 = Rectangle(100, 200)
    a2 = Rectangle(100, 100)
    print(a1.area())
    print(a2.perimeter())


# 定义以下类：
#
# 1. `Shape` 基类，有 `area()` 和 `perimeter()` 方法（返回 None）
# 2. `Circle` 继承 `Shape`，有 `radius` 属性
# 3. `Rectangle` 继承 `Shape`，有 `width` 和 `height` 属性
# 4. 测试计算圆和矩形的面积
def p2():
    class Shape:
        def __init__(self):
            pass
        def area(self):
            return None
        def perimeter(self):
            return None
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return math.pi*self.radius**2

    class Rectangle(Circle, Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def area(self):
            return self.width*self.height

    c = Circle(100)
    p = Rectangle(100, 200)
    print(c.area())
    print(p.area())

# 实现 `Range` 类，模拟 `range()` 的行为：
#
# 1. `__init__(start, stop)`
# 2. `__iter__()` 返回自身
# 3. `__next__()` 返回下一个值
# 4. 测试：`for i in Range(1, 5): print(i)`

def p3():
    class Range:
        def __init__(self, start, stop):
            self.start = start
            self.stop = stop
        def __iter__(self):
            return self
        def __next__(self):
            if self.start < self.stop:
                self.start += 1
                return self.start-1
            else:
                raise StopIteration
    for i in Range(1, 5):
        print(i)



# 编写生成器函数 `even_numbers(n)`：
#
# 1. 产出 0 到 n 之间的所有偶数
# 2. 测试：`for num in even_numbers(10): print(num)`

def p4():
    def even_numbers(n):
        i = 0
        while i <= n:
            if i % 2 == 0:
                yield i
            i += 1
    for num in even_numbers(10):
        print(num)


# 实现 `BankAccount` 类：
#
# 1. `__init__(owner, balance=0)`：开户
# 2. `deposit(amount)`：存款
# 3. `withdraw(amount)`：取款（余额不足时抛异常）
# 4. `get_balance()`：查询余额
# 5. `__str__()`：返回账户信息

def p5():
    class BankAccount:
        def __init__(self, balance=0):
            self.balance = balance
        def deposit(self, amount):
            self.balance += amount
        def withdraw(self, amount):
            if self.balance - amount < 0:
                raise ValueError("余额不足")
            self.balance -= amount

        def get_balance(self):
            return self.balance

        def __str__(self):
            return f"账户剩余: {self.balance}元"

    b = BankAccount()
    b.deposit(100)
    b.withdraw(10)
    print(b)
    try:
        b.withdraw(100)
    except ValueError as e:
        print(e)

p5()
# 实现以下类：
#
# 1. `Student`：有 `name`、`scores`（字典）属性
# 2. `add_score(subject, score)`：添加成绩
# 3. `get_average()`：计算平均分
# 4. `StudentManager`：管理多个学生
# 5. `add_student(student)`：添加学生
# 6. `get_top_student()`：找出最高平均分的学生


# 实现简单的链表：
#
# 1. `Node` 类：有 `value` 和 `next` 属性
# 2. `LinkedList` 类：有 `head` 属性
# 3. `append(value)`：添加节点
# 4. 实现 `__iter__()` 使其可以 for 循环遍历


