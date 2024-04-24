'''
    定义字典
'''

# dictionary   ->dict
dict = {}
print(dict)
print(type(dict))

d = {1:'one', '2':'two'}
print(d)

d = {'one':'星期一', 'two':'星期二', 'three':'星期三', 'four':'星期四','five':'星期五', 'heihei':'星期六', 'haha':'星期天'}
print(d)

# 字典的访问
print(d['one'])
print(d['haha'])

# 字典是一个可变的数据类型
d['haha'] = '星期一'
print(d['haha'])


# 字典的遍历
# 方式一
for v in d:
    print(v)

# 方式二
for v in d.keys():
    print(f"{v}----{d[v]}")


print(d.values())
# 方式三
for v in d.values():
    print(f"value-{v}")

# 方式四
for item in d.items():
    print(f"item[0]--{item[0]},item[1]--{item[1]}")

for k,v in d.items():
    print(f"item:{k}--->{v}")

print('---------')
# 解包
item = (1,2,3,4,5)
a,b,c,d,e = item
print(a)
print(e)

'''
    字典的增删改查
'''
print('字典的增删改查')

d = {}

# 增
# 如果在赋值时，使用的key在字典中不存在，那么就是向字典中添加  数据
d['name'] = 'sunn'
d['age'] = 18
print(d)

# 改
# 如果是赋值时，使用的key在字典中存在，那么就修改这个key所对应的值
# 字典中的key，具有唯一性  如果key不存在，那么就是添加数据

# 查
print(d['name'])
print(d.get('name'))

# 删除   popitem()：删除最后一个键值对
# d.popitem()
# print(d)
# d.popitem()
# print(d)

# pop(key) 可以制定删除某个key值
d.pop('name')
print(d)

# 清空字典中的键值对    d.clear()
# d.clear()
# print(d)

# del
del d['age']
print(d)


