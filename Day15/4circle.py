"""
输入半径计算圆的周长和面积

Author: Junjie
Date:2019-05-06

"""

import math
# import random


radius = float(input('请输入圆的半径; '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)
print('周长和面积')