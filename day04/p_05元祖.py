'''
    元祖的定义和下标使用
'''

# 定义一个空元祖
t1 = ()
print(t1)
print(type(t1))

# 定义包含元素的元祖
t2 = ('aa', 2, 4, 'sunn')

# 定义包含其它数据类型的元组
t3 = ('a','b','hello','world')

# 元组的复杂定义形式
t4 = (1, 3.14, 'Hello', True, t3)

# 定义具有一个元素的元组,特殊，注意，重点   一个元素必须要加 ,
t5 = (1, )
print(t5)
print(type(t5))

# 使用类型名定义元祖
t6 = tuple()
print(type(t6))

t7 = tuple('hello')
print(t7)

# 元组的下标访问
t8 = (1,2,3,4,5,6,7,8)
print(t8[0])
print(t8[3])
print(t8[7])
# 元组也不能使用超出范围的下标，会出现越界错误
# print(t8[70])  #　IndexError: tuple index out of range

# 元组是一种 不可变类型，不能修改元组中的元素值 ，修改会报错
# t8[0] = 1111  #TypeError: 'tuple' object does not support item assignment

print('元祖的遍历\n')
'''
    元祖的遍历
'''

last_name = tuple('红力')
first_name = tuple('王')

t = (1,2,3,4,'hello')
for v in range(len(t)):
    val = t[v]
    print(val)


i = 0
while i< len(t):
    print(t[i])
    i += 1

print('元祖的嵌套及遍历')
'''
    元祖的嵌套及遍历
'''

t = (1,2,3,(5,6,7),4,4,(7,8,9))
for v in t:
    if isinstance(v, tuple):
        for v2 in v:
            print(v2)
    else:
        print(v)


'''
    元祖常用的方法
'''

t = (1,2,3,4,5,5,67)
print(t.count(2))
print(t.index(2))
print(t.index(2,0,5))