'''
_______________#########_______________________ 
______________############_____________________ 
______________#############____________________ 
_____________##__###########___________________ 
____________###__######_#####__________________ 
____________###_#######___####_________________ 
___________###__##########_####________________ 
__________####__###########_####_______________ 
________#####___###########__#####_____________ 
_______######___###_########___#####___________ 
_______#####___###___########___######_________ 
______######___###__###########___######_______ 
_____######___####_##############__######______ 
____#######__#####################_#######_____ 
____#######__##############################____ 
___#######__######_#################_#######___ 
___#######__######_######_#########___######___ 
___#######____##__######___######_____######___ 
___#######________######____#####_____#####____ 
____######________#####_____#####_____####_____ 
_____#####________####______#####_____###______ 
______#####______;###________###______#________ 
________##_______####________####______________ 

Descripttion: CRAPS赌博游戏
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的
桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子
获得点数进行游戏。简单的规则是：玩家第一次摇骰子如果
摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点
或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出
了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜
；其他点数，玩家继续要骰子，直到分出胜负。
version: 0.1
Author: 崩布猪
Date: 2024-02-17 19:06:33
LastEditors: 崩布猪
LastEditTime: 2024-02-17 19:22:32
'''

# 我们设定玩家开始游戏时有1000元的赌注
# 游戏结束的条件是玩家输光所有的赌注

from random import randint

money = 1000
while money > 0:
    print('哦我的老伙计，现在还有 %d ' % money)
    needs_go_on = False
    while True:
        debt = int(input('请下注:'))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('您摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜利')
        money += debt
    elif first == 2 or first == 3 or  first == 12:
        print('庄家胜利')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True
print('你破产了, 游戏结束!')
      