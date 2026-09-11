arr = [x ** 2 for x in range(10)]
print(arr)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# transposed = []
# for i in range(4):
#     print(i)
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     print(transposed_row)
#     transposed.append(transposed_row)

print([[row[i] for row in matrix] for i in range(4)])


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

d = {'a': 1, 'b': 2, 'c': 3}
keys = list(d)
print(keys)


nums = [10, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nums = set(nums)

print(sorted(nums))

nums10 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print([x for row in nums10 for x in row])

nums = [(1, 'a'), (2, 'b'), (3, 'c')]
print(dict([(y,x) for x,y in nums]))

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0)+1
print(freq)

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
print(dict([(x,y) for x,y in zip(names, ages)]))


d = {'a': 1, 'b': None, 'c': 3, 'd': None, 'e': 5}
for key,value in d.copy().items():
    if value is None:
        del d[key]
print(d)

print(list(reversed([(x,y) for x,y in enumerate('abc')])))
print(sorted(set("aaahhhhdddbbb")))


text = "the quick brown fox jumps over the lazy dog the fox"
nums = text.split()
freq = {}
for x in nums:
    freq[x] = freq.get(x,0)+1
print(freq)
print(max(freq,key=freq.get))
print(sorted(freq,key=freq.get,reverse= True))
print([x for i,x in enumerate(sorted(freq,key=freq.get, reverse=True)) if i <3] )


data = [
    ('Math', 'Alice', 90),
    ('Math', 'Bob', 85),
    ('English', 'Alice', 88),
    ('English', 'Bob', 92),
    ('Math', 'Charlie', 78),
    ('English', 'Charlie', 80),
]
dic = {}
for x,y,z in data:
    print(x,y,z)
    dic[x] =dic.get(x, [])
    dic[x].append(z)
