'''
    对齐
    center()    按给定宽度居中显示
    rjust()     右对齐
    ljest()     左对齐

    strip()     去除两端空白
    lstrip()    去除左侧空白
    rstrip()    去除右侧空白
'''

s = 'Hello'
print(s)
print('|' + s.center(11) + '|')

# r -> right
print('|' + s.rjust(11) + '|')
print('|' + s.rjust(11,'_') + '|')


# l -> left
print('|' + s.ljust(11) + '|')
print('|' + s.ljust(11,'_') + '|')

s = '    Hello     world   '
print(s)

print('|' + s.strip() + '|')
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')

ret = s.split()
ret = ''.join(ret)
print('|' + ret.center(21) + '|')


print(5.0 // 3)