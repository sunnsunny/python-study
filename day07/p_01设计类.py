'''
    类
'''

class Hero:
    def skill(self):
        print('发一个大招')

class Person:
    def set(self, food):
        print('吃', food)

    def sleep(self):
        print('每天至少睡8小时')

class Dog(object):
    def bark(self):
        print(self.name, self.hair,'Wow Wow...')

tom = Dog()
tom.name = 'duoduo'
tom.hair = 'red'

tom.bark()

tom.bark()
