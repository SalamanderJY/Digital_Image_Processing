# -*- coding: UTF-8 -*-

import os

for d in os.listdir('.'):   # os.listdir可以列出文件和目录
    print d
'''

'''
list(range(1, 11))

L = []
for x in range(1, 11):
    L.append(x * x)

[x * x for x in range(1, 11)]

[x * x for x in range(1, 11) if x % 2 == 0]

# 使用两层循环，可以生成全排列
[m + n for m in 'ABC' for n in 'XYZ']



