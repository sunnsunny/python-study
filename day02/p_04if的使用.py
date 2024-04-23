'''
    if的使用
'''

def is_net_connected(age):
    if age >= 18:
        print('可以上网')
    else:
        print('不可以上网')

# age = int(input('请输入年龄'))
# is_net_connected(age)


def is_even_number(num):
    if num % 2 == 0:
        print('是偶数')
    else:
        print('不是偶数')


is_even_number(3)
is_even_number(4)

# if elif else  使用
def is_week_day(day):
    if day == '1' or day == '一':
        print('今天是星期一')
    elif day == '2' or day == '二':
        print('今天是星期二')
    elif day == '3' or day == '三':
        print('今天是星期三')
    elif day == '4' or day == '四':
        print('今天是星期四')
    elif day == '5' or day == '五':
        print('今天是星期五')
    elif day == '6' or day == '六':
        print('今天是星期六')
    elif day == '7' or day == '七':
        print('今天是星期七')
    else:
        print('输入不对')


d = input('input:')
is_week_day(d)

#  if的嵌套

def is_score_level(score):
    if score >= 0 and score <= 100:
        if score < 60:
            print('差')
        elif score < 80:
            print('良')
        else:
            print('优')
    else:
        print('输入无效')

is_score_level(90)