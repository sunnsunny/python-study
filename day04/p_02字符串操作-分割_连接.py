'''
    分割_连接
    split()
    splitlines
    partition
    rpartition
    join
'''

s = 'Hello world Hello world Hello world Hello world Hello Sunno'

def test_split():
    ret = s.split(' ')
    print(ret)
    print(type(ret))

    ret = s.split('o')
    print(ret)

    ret = s.split('o', 2)
    print(ret)

    ss = 'Hello\tWorld Hello \t\nWorld Hello\n Python'
    print(ss)
    # 如果在分割字符串时，需要使用任何空白进行分割，那么参数中，什么也不需要写
    print(ss.split())

# test_split()

# splitlines 按行分割
def test_splitlines():
    ss = 'Hello\tWorld Hello \t\nWorld Hello\n Python'
    print(ss.splitlines())
    print(ss.split('\n'))

# test_splitlines()



# partition 分割  : 保留切割
# 按分割条件将字符串分割成三部分，分割条件前，分割条件，分割条件后
def test_partition():
    ss = 'HellohahaHelloHellohahaHello'
    print(ss.partition('haha'))


    # rpartition() 从右侧进行分割
    ss = 'HellohahaHelloHellohahaHello'
    print(ss.rpartition('haha'))

# test_partition()


# join() 使用当前字符串连接参数中的每个元素

def test_join():
    ss = 'Hello World Python'
    print('-'.join(ss))

    # join 的作用
    s_ss = ss.split()
    print(s_ss)
    # j_ss = '$'.join(s_ss)
    j_ss = '_'.join(s_ss)
    print(j_ss)

    print('$'.join('ABCd$'))


test_join()