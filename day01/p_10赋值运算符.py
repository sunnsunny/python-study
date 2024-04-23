'''
    赋值运算符
'''

a = 1
b = "hello"

a = 2
b = 3
a += b
print(a, b)

a = 2
b = 3
# 这个类似 a = a * (b + 5)
a *= b+5
print(a)