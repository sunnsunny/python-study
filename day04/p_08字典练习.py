'''
    字典练习
    建立名片
    显示名片-->接受谁打印谁
'''

def creat_card():
    card = {}
    card['name'] = input('请输入名字')
    card['age'] = input('请输入年龄')
    card['weight'] = input('请输入体重(kg)')
    card['address'] = input('请输入地址')
    return card

def show_card(card):
    for k in card:
        print(f"k:{k},v:{card[k]}")

show_card(creat_card())