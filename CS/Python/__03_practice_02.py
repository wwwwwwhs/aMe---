"""
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

Descripttion:分段函数求指
         3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
version: 0.1
Author: 崩布猪
Date: 2024-02-16 17:19:34
LastEditors: 崩布猪
LastEditTime: 2024-02-16 17:19:47
"""
x = float(input('请输入x：'))
if x > 1:
   y = 3 * x  - 6
elif x >= -1 and x <= 1:
   y = x + 2
else:
   y = 5 * x + 3
print ('f(%.2f) = %.2f' % (x, y))
        

   
