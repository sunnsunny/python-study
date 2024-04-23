'''
    函数
'''

def say_hi(name):
    print(f"Hello {name}")

def sum_number(a, b):
    print(a + b)

def get_name():
    return "sunn"

say_hi("sunn")
sum_number(3, 4)
print(f"Hello, {get_name()}")


print("--------")

def get_keyb_num():
    print("请输入一个number:")
    rel = input()
    return int(rel)

# a = get_keyb_num()
# b = get_keyb_num()
# print(a + b)


def get_num():
    return 1
    return 2
    return 3

print(get_num())