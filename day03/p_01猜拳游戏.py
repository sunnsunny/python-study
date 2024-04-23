'''
    猜拳游戏
'''

import random

def foot_game(total):
    print('游戏开始：')
    _is_begin = True
    _user = 0
    _system_ = 0
    _user_count = 0
    _sys_count = 0
    while(_is_begin):
         if _user_count + _sys_count == int(total):
            if _user_count > _sys_count:
                print('最终玩家胜利')
            elif _user_count == _sys_count:
                print('平局')
            else:
                print('最终电脑胜利')
            break

         _inp = input('请输入:（0：石头 1：剪刀  2：布  q:退出）')
         if _inp == 'q':
             print('欢迎下次再来')
             break

         _user = int(_inp)
         if not (_user>=0 and _user<=2):
             print('输入不合法，请重新输入')
             continue;

         _system_ = int(random.randint(0, 2))
         if ((_user==0 and _system_==1) or (_user==1 and _system_==2) or (_user==2 and _system_==0)):
             print('玩家胜利!')
             _user_count += 1
         else:
             print('电脑胜利!')
             _sys_count += 1
         print(f"当前比分玩家比系统：{_user_count}比{_sys_count}")



total_num = input("请输入总共局数:")
foot_game(total_num)



