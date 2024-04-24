'''
    列表推导式
    创建一个具有一百个数字的列表
'''
import random

c_l = []
for i in range(100):
    c_l.append(i)

# print(c_l)

# 使用推导式来完成列表创建
c_l = [i for i in range(100)]
# print(c_l)

# 1到101 3的倍数的列表
c_l = [x for x in range(1, 101) if x % 3 == 0]
# print(c_l)

# 创建一个列表，列表中的每个元素都是具有两个值的元祖
# c_l = [(x, x) for x in range(10)]
# c_l = [(x,) for x in range(10)]
c_l = [(x, y) for x in range(10) for y in range(3)]
# print(c_l)

a = 1,2,3,4,5
print(a)
print(type(a))

# 拆包
# 注意：拆包时，容器中的元素个数要和变量个数相同
# a1,a2,a3,a4,a5 = a
# a1,a2,a3,a4,a5 = [1,2,3,4,5]
# a1,a2,a3,a4,a5 = 'abcde'
a1,a2,a3,a4,a5 = {'a':1,'b':2,'c':3,'d':4,'e':5}
print(a1,a2,a3,a4,a5)