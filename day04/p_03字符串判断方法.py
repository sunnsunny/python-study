'''
    startswitch()   判断是否是以制定字符串开头
    endswitch()     判断是否是以制定字符串结束
    isupper()       判断是不是大写字符
    islower()       判断是不是小写字符
    isdigit()       判断是不是数字字符
    isalpha()       判断是不是字母
    isalnum()       判断是不是字母或者数字字符
    isspace()       判断是不是空白字符，包含空格，换行符\n，制表符\t，注意'' 字符串不是空白字符
'''

def test_startwith():
    print('18280066008'.startswith('182'))
    print('18280066008'.startswith('1823'))

# test_startwith()

def test_endwith():
    print('www.xxx.gov.com'.endswith('gov'))
    print('www.xxx.gov'.endswith('gov'))

# test_endwith()

def test_other():
    # print('hello'.isupper())
    # print('Hello'.isupper())
    # print('HELLO'.isupper())

    # print('hello'.islower())
    # print('Hello'.islower())
    # print('HELLO'.islower())

    # print('hello'.isalpha())
    # print('Hello'.isalpha())
    # print('HELLO'.isalpha())
    # print('123'.isalpha())
    # print('abc123'.isalpha())
    #
    # print('HELLO'.isalnum())
    # print('123'.isalnum())
    # print('abc123'.isalnum())
    # print('abc 123'.isalnum())

    # print('HELLO'.isdigit())
    # print('123'.isdigit())
    # print('abc123'.isdigit())
    # print('123abc'.isdigit())

    print(''.isspace())
    print(' '.isspace())
    print('\t'.isspace())
    print('\n'.isspace())

# test_other()

def str_switch():
    s = 'Hello world Hello world Hello world Hello sunn'
    # print(s.upper())
    print(s.lower())
    # 所有单词都是大写开头，其他部分都是小写
    print(s.title())
    # 所有单词  第一个字母变成大写，其他都变成小写
    print(s.capitalize())

str_switch()