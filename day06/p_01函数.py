'''
    函数
'''

def show():
    print('Hello sunn!')

show()

func = show
print(func)
func()

def display():
    print('Display run')

def call_function(func):
    func()

call_function(show)
call_function(display)


'''
    匿名函数
'''

func = lambda  : 1 + 1
print(func)
print(func())


# lambda 定义时的注意事项
# 1. lambda　默认返回表达计算结果，不需要return ,如果加了reutrn 反而报错
# func = lambda x, y: return x + y

# 2. 不能使用 循环
# func = lambda x,y: for i in range(x, y): print(i)
# func = lambda x,y: i = x while i < y: print(i) i +=1


# 3. 不能使用if的正常格式
# func = lambda n: if n % 2 == 0: print('偶数')

# 4. 但是可以使用 if实现的三目运算符
func = lambda m, n: m if m > n else n

print(func(11, 2))
