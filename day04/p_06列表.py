'''
    列表的定义和下标访问
'''

# 定义一个空列表
cl = []
print(cl)
print(type(cl))

# 定义具有一个元素的列表
cl2 = [1,]
print(cl2)
print(type(cl2))

# 定义具有多个元素的列表
cl3 = ['sunn', 'Hello', (3,4,5),['a', 'b', 'c']]
print(cl3)
print(type(cl3))


for v in cl3:
    if isinstance(v, tuple) or isinstance(v, list):
        for v2 in v:
            print(v2)
    else:
        print(v)

# 使用list()创建 列表 对象
# cl4 = list()  # 空列表
cl4 = list('hahaha')
print(cl4)
print(type(cl4))

# 通过下标访问列表中的元素
cl5 = [1, 2, 3, 4, 5]
print(cl5[0])
print(cl5[3])
print(cl5[4])
# print(cl5[10]) #IndexError: list index out of range


# 重点：列表 的特性，可以通过 下标修改对应位置上的数据
print(cl5)
cl5[0] = 999
print(cl5)

# 字符串逆序
s = 'hello'


def revers_str(s):
    # 定义一个空字符串，用来拼接
    ret_s = ''
    i = len(s) - 1
    while i >= 0:
        ret_s += s[i]
        i -= 1

    return ret_s


print(revers_str(s))


'''
列表 的排序和逆序
'''

cl = [9,2,5,7,1,8,4,3,0,6]

print(cl)
# 排序 默认升序排序（从小到大）
print(cl.sort())
print(cl)


cl = [9,2,5,7,1,8,4,3,0,6]
# 降序排序 （从大到小）
cl.sort(reverse=True)
print(cl)


# 逆序
cl = [9,2,5,7,1,8,4,3,0,6]

# 逆序是直接将原列表中的顺序进行逆转
cl.reverse()
print(cl)



# 实现列表逆序方法
def reverse_list(cl):
    # 定义一个空列表
    ret_l = []
    i = len(cl) - 1
    while i >= 0:
        ret_l.append(cl[i])  # s += c
        i -= 1

    return ret_l

print(reverse_list(cl))


'''
l = [1,2,3,4,5]
l[0]
l[4]
l = [5,2,3,4,1]
l[1]
l[3]
l = [5,4,3,2,1]





'''



'''
增：
			append()
			extend()
			insert()
'''

# append 追加数据
cl = []
cl.append(1)
cl.append(2)
cl.append(3)
cl.append('hello')
print(cl)
cl.append(['a','b'])
print(cl)

# extend() 扩展
# 可以将参数中的容器对象中的每个元素添加扩展到源列表中
cl1 = [1,2,3]
cl2 = ['a','b','c',[5,6]]
# cl1.append(cl2)
cl1.extend(cl2)
print(cl1)


# insert 插入
cl3 = [1,2,3,4,5]
cl3.insert(0,999)
print(cl3)
cl3.insert(2,888)
print(cl3)
cl3.insert(7,777)
print(cl3)

# 注意：在插入数据时，没有下标越界问题
# 如果指定下标超过元素正常范围，相当于追加
cl3.insert(17,666)
print(cl3)

'''
列表 操作-查找
'''

l = [1,2,3,4,5,6,6,6,6,6,2,3]

# count()
print(l.count(6))
print(l.count(66))

# index()
print(l.index(6))
print(l.index(2))
# print(l.index(22))  # ValueError: 22 is not in list

# in - not in
print(2 in l)
print(22 in l)

print(2 not in l)
print(22 not in l)

'''
删：
			pop（）
			remove()
			clear() 清空但列表存在
			del 全没了
'''

cl = [1,2,3,4,5,6,7,3,7,8,90,91,0]

# pop()
# pop 中的 index 参数可以不写，默认删除 最后一个
cl.pop()
print(cl)

cl.pop(0)
print(cl)

# remove
# 删除 指定对象，当有多个相同对象时，只删除 第一个
cl.remove(7)
print(cl)


# del 有两种 方式

del cl[1]
print(cl)

del(cl[1])
print(cl)

# 将整个列表删除
# del cl
# del(cl)

print(cl) #NameError: name 'cl' is not defined


# clear()
# 清空列表元素

cl.clear()
print(cl)

# 在使用列表时，不要在循环遍历时删除元素

cl = [5, 3, 8,91]

for o in cl:
    cl.remove(o)

print(cl)



