'''
    查找，替换，统计
    find()
    rfind()
    index()
    rindex()
    replace()
    count()
'''

s = "oaooooarld hello world hello sunn hello world"

# find
def str_find():
    idx = s.find('orld')
    print(idx)

    idx = s.find('orld', 8, 20)
    print(idx)


def str_index():
    idx = s.index('orld')
    print(idx)

    idx = s.index('orld', 8, 20)
    print(idx)

def test_rfind_rindex():
    # 最后出现字母o的下标
    print(s.rfind('o'))
    print(s.rindex('o'))

    print(s.rfind('kk'))
    print(s.rindex('kk'))


def str_replace():
    print(s.replace('l', 'L'))
    print(s)

    print(s.replace('l', 'L', 3))

def str_count():
    print(s.count('o'))
    # 从初始位置到结束为止包含o的个数，  这个为止包含1 到 5截止，不包含5
    print(s.count('o', 1, 5))

# str_find()
# str_index()
# test_rfind_rindex()
# str_replace()
str_count()