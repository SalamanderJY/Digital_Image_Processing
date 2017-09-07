# -*- coding: UTF-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']

print classmates

print len(classmates)

print classmates[0], classmates[1], classmates[2]

print classmates[-1], classmates[-2], classmates[-3]

classmates.append('Adam')

classmates.insert(1, 'Jack')

classmates.pop()

classmates.pop(1)

classmates[1] = 'Sarah'

L = ['Apple', 123, True]

s = ['python', 'java', ['asp', 'php'], 'scheme']
# 要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']

L = []
len(L) # 0