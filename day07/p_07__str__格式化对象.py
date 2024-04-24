'''
    __str__() 方法
'''

class Cat(object):
    def __init__(self, name, age, height):
        self.username = name
        self.age = age
        self.height = height

    # 默认没有实现 __str__方法，那么会打印　<模块名．类名　object at 0x...>
    # 如果想按自己的格式 显示，需要在类中实现 该 方法
    def __str__(self):
        print('str run...', self.username)
        s = self.username + str(self.age).ljust(5) + self.height.ljust(5)
        return s

tom = Cat('tom', 5, '50cm')
print(tom)