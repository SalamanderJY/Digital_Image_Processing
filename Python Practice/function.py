import math

from func import move
from func import my_abs

my_abs(1)

abs(100)

abs(-20)

abs(12.34)

max(1, 2)

max(2, 3, 1, -5)

int('123')

int(12.34)

float('12.34')

str(1.23)

str(100)

bool(1)

bool('')

a = abs  # 变量a指向abs函数
a(-1)  # 所以也可以通过a调用abs函数

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)
