#
# 1. 用 `try/except` 捕获 `1/0` 的异常
# 2. 打印异常类型和信息
def p1(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f"发生错误了{e}")


# 1. 循环要求用户输入数字
# 2. 输入非数字时提示重新输入
# 3. 输入负数时抛出自定义异常
# 4. 输入正确数字后退出循环
class NegativeNumberError(Exception):
    pass

def p2():
    while True:
        try:
            a = int(input())
            if a<0:
                raise NegativeNumberError("不能是负数")
            print("输入正确")
            break
        except ValueError:
            print("请输入有效的整数")
        except NegativeNumberError as e:
            print(f"错误：{e}")

# 1. 定义函数 `read_config(filename)`
# 2. 文件不存在时，捕获 `FileNotFoundError`
# 3. 抛出 `RuntimeError("配置加载失败")` 并用 `from` 链接原始异常

def p3():
    try:
        with open("12.txt","r",encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError("配置加载失败") from e

try:
    p3()
except RuntimeError as e:
    print(f"错误：{e}")
    print(f"原因：{e.__cause__}")



# 定义以下异常类：
#
# 1. `ValidationError`：数据验证错误，包含字段名和错误信息
# 2. `AgeError`：年龄错误（继承 `ValidationError`）
# 3. 编写函数 `validate_age(age)`，年龄不在 0-150 范围内时抛出异常

class ValidationError(Exception):
    def __init__(self,field, message):
        self.field = field
        self.message = message
        # super()调用父类 Exception 的构造函数，把错误信息传上去,否则打印就只有类名，没有消息
        super().__init__(f"{field}:{message}")

class AgeError(ValidationError):
    def __init__(self,age,message):
        self.age = age
        super().__init__("age",message)
def p4(age):
    try:
        age = int(age)
        if age<0 or age>150:
            raise AgeError(age, "年龄超出范围")
    except AgeError as e:
        print(e)
p4(-1)
