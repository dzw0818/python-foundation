import datetime

products = [
    ("笔记本电脑", 5999.5),
    ("鼠标", 129.0),
    ("键盘", 299.9),
]
print(f"商品名称      价格")
for name, price in products:
    print(f"{name:<10}{price:>10.2f}")


import json
data = {"name": "Tom", "scores": [90, 85, 92]}
s = json.dumps(data, ensure_ascii=False)
print(s)


# 编写代码：
#
# 1. 创建文件 `diary.txt`，写入今天的日期和一行日记
# 2. 再追加一行日记
# 3. 读取并打印全部内容

def p1():
    with open("diary.txt", "w", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()}:又是学习的一天\n")
    with open("diary.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()}:要坚持\n")
    with open("diary.txt", "r", encoding="utf-8") as f:
        print(f.read())



# 编写一个"通讯录"程序：
#
# 1. 定义联系人数据（字典形式）
# 2. 保存到 `contacts.json`
# 3. 从文件读取并打印

def p2():
    contacts = {
        "Alice": {"phone": "13800001111", "email": "alice@example.com"},
        "Bob": {"phone": "13800002222", "email": "bob@example.com"},
    }
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(contacts,f,ensure_ascii=False,indent=2)

    with open("contacts.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for k, v in data.items():
            print(f"{k:<10}{v}")



# 编写代码：
#
# 1. 创建文件 `numbers.txt`，每行写一个数字（1到10）
# 2. 读取文件，计算所有数字的总和
# 3. 打印结果

def p3():
    with open("numbers.txt", "w", encoding="utf-8") as f:
        for n in range(1,11):
            f.write(f"{n}\n")

    sum = 0
    with open("numbers.txt", "r", encoding="utf-8") as f:
        for n in f:
            sum+=int(n.strip())
    print(sum)




# 编写程序：
#
# 1. 用列表存储消费记录：`[{"item": "午餐", "price": 35}, ...]`
# 2. 保存到 JSON 文件
# 3. 读取后计算总消费
# 4. 用 f-string 格式化输出每条记录和总计

def p4():
    records = [
        {"item": "午餐", "price": 35},
        {"item": "咖啡", "price": 28},
        {"item": "地铁", "price": 5},
        {"item": "晚餐", "price": 42},
    ]
    with open("records.json", "w", encoding="utf-8") as f:
        json.dump(records,f,ensure_ascii=False,indent=2)

    with open("records.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        print(f"{'项目':<10}{'价格':>10}")
        sum = 0
        for item in data:
            print(f"{item['item']:<10}{item['price']:>10.2f}")
            sum+=item['price']
        print(f"总花费：{sum:.2f}元")


# 1. 保存到 JSON 文件
# 2. 读取并计算每个学生的总分和平均分
# 3. 格式化输出成绩表
def p5():
    students = [
        {"name": "Alice", "scores": {"语文": 85, "数学": 92, "英语": 88}},
        {"name": "Bob", "scores": {"语文": 78, "数学": 95, "英语": 82}},
    ]
    with open("students.json", "w", encoding="utf-8") as f:
        json.dump(students,f,ensure_ascii=False,indent=2)
    print(f"{'姓名':<10}{'总分':>10}{'平均分':>10}")
    for s in students:
        total = sum(s["scores"].values())
        avg = total / len(s["scores"])
    # for student in students:
    #     sum,avg = 0,0
    #     for k, v in student['scores'].items():
    #         sum+=int(v)
    #     avg = sum/len(student['scores'])
        print(f"{s['name']:<10}{total:>10}{avg:>10.2f}")

p5()

