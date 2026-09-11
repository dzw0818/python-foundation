# # ---------1、if
# x = int(input("输入一个数字："))
# if x < 10:
#     print("这个数比10小")
# elif x >= 10:
#     print("这个数大于等于10")

# -----------2、for
# 2.1、你的 users 类型	应该怎么写
# 字典 {'a':1, 'b':2}	for key, value in users.items():
# 列表 ['a', 'b', 'c']	for item in users:
# 列表的元组 [('a',1), ('b',2)]	for key, value in users:
# 列表的元组（3个元素）[('a',1,2)]	for a, b, c in users: 或 for a, b, _ in users:
# 列表的字典 [{'a':1}, {'b':2}]	for item in users: 然后 item['a']
words = ['cat', 'window', 'defenestrate']
for item in words:
    print(item)

scores = {'张三': 85, '李四': 92, '王五': 78}
# for key in list(scores.keys()):
#     if scores.get(key) < 80:
#         del scores[key]
# print(scores)
# 推导式
scores = {k:v for k,v in scores.items() if v >= 80}
print(scores)

data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in data:
    print(a + b + c)

# 2.2、在循环字典时不能修改字典的长度（但是可以改变里面的值，策略就是建一个新的字典
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# 推导式
user = {k:v for k,v in users.items() if v == 'active'}
# 复制一个新字典，删除旧字典数据
for key,value in users.copy().items():
    if value == 'inactive':
        del users[key]
print(users)
# 新建一个字典，存新数据
new_users = {}
for key,value in users.items():
    if value == 'active':
        new_users[key] = value
print(new_users)

# 删除所有库存小于5的商品
inventory = {'apple': 10, 'banana': 5, 'orange': 8, 'grape': 3}
for key,value in inventory.copy().items():
    if value < 5:
        del inventory[key]
print(inventory)

# 打印名字和年龄
people = [('张三', 25, '北京'), ('李四', 30, '上海'), ('王五', 28, '广州')]
for item in people:
    a,b,_ = item
    print(a,b)
# 打印active为true的名字
users = [
    {'id': 1, 'name': 'Alice', 'active': True},
    {'id': 2, 'name': 'Bob', 'active': False},
    {'id': 3, 'name': 'Charlie', 'active': True}
]
for item in users:
    if item['active']:
        print(item['name'])

# -----------3、range() 生成等差数列
for i in range(5, 10, 2):
    print(i)



# -----------4、函数参数
def register(username, password, email=None, phone=None):
    print(f"username={username}, password={password}, email={email}, phone={phone}")

register("david", "xyz789", phone="13800138000", email="123")