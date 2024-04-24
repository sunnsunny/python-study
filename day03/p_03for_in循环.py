'''
    for-in循环使用
'''

def test_func1():
    for c in 'sunn':
        print(c.upper())


# test_func1()

def test_func2():
    for _ in range(10, 20):
        print("hello", _)

def test_func3():
    str = "Hello sunn"
    for v in range(0, len(str)):
        val = str[v]
        print(val)


    # test_func2()

test_func3()
