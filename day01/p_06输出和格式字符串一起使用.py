'''
    格式化字符串并输出
'''
# 占位符形式的字符串
a = 10
print("现在要打印一个a的值：%d" % a)

print("names: %s age: %d " % ("sunn", 32))

print("%d" % 1)
print("%5d" % 1)
print("%05d" % 1)
print("%-5d" % 1)
print("%3d" % 1234578)

print("%.3f" % 3.1415926)
print("%.3f" % 1)

# f-string
name = "sunn"
age = 32
print(f"name:{name},age:{age},score:{99}")

s = f"name:{name},age:{age},score:{99}"
print(s)