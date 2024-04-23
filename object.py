a = 3
print(id(a))
print(type(a))

b = "Hello Sunn"
print(id(b))
print(type(b))

print("b:" + b)

print("----------------------------------")

a = 123
b = 3.14
b2 = 314e-3
d = "Hello world"
print(type(a))
print(type(b))
print(type(b2))
print(type(d))
print("bb" + str(b))


'''
    sunn
    运算符
    +加号，-减号，*乘法，/浮点整除法,// 整数除法，%取模运算符，**幂：2**3 = 8
    
'''

print(9/2)
print(9//2)

# 返回一个元祖 (4, 1) (商，余数)
rel = divmod(13, 3)
print(rel[0])

print("整数---------------------------------------------")
# 整数：无限大 不会溢出

# 二进制   0b或者0B开头
# 八进制   0o或者0O开头
# 十六进制  0x或者0X开头
a = 0b010101
b = 0o11
c = 0xff

# 浮点数
