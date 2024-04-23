'''
    传入一个数字，来控制输出的次数，倒序输出数字
'''

def print_num(num):
    i = num
    while i>0:
        print(i)
        i -= 1



# print_num(10)



'''
输出下列图形：
1
12
123
1234
12345

输出行数由参数控制
'''

def print_graph():
    i = 1
    while i < 6:
        # print("*"*i)
        j = 0
        rel = ''
        while j<i:
            j += 1
            rel += str(j)

        print(rel)
        i += 1

print_graph()



'''
打印99乘法表
'''

print('\n\n')
def nine_nine_table():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print('%d*%d=%-3d' % (j, i, j*i), end='   ')
            j += 1
        print()
        i += 1



nine_nine_table()