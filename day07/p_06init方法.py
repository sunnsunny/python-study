'''
    init方法
    该方法会在创建对象是自动调用
    并对该对象进行初始化操作
'''

class Cat(object):
    def __init__(self, name, age):
        print('Init Run ...', self)
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


tom = Cat('tom', 1)
print(tom)
tom.show()

# 在调用 方法时，方法的第一个参数 self 是不用手动传参的
# 这个参数会由解释 器自动将调用 该 方法的对象传递过去



def show():
    a = 1
    print(id(a))
    return a

b = show()
print(b)
print(id(b))