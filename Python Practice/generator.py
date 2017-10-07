# -*- coding: UTF-8 -*-

L = [x * x for x in range(10)]

g = (x * x for x in range(10))

for n in g:
    print(n)


def fib(maxvalue):
    i, a, b = 0, 0, 1
    while i < maxvalue:
        print(b)
        a, b = b, a + b
        i = i + 1
    return 'done'


def generator(maxvalue):
    i, a, b = 0, 0, 1
    while i < maxvalue:
        # yield b
        a, b = b, a + b
        i = i + 1
    return 'done'

'''
g = fib(6)
while True:
    try:
         x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
'''




