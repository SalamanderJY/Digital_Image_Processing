# -*- coding: UTF-8 -*-

print('I\'m ok.')

print('I\'m learning\nPython.')

print('\\\n\\')

print('\\\t\\')
# Python还允许用r''表示''内部的字符串默认不转义
print(r'\\\t\\')

print('''line1
line2
line3''')

a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

print('包含中文的str')

print ord('A')
# python 3
# print ord('中')

#print chr(25991)

# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

print 'ABC'.encode('ascii')

print len('中文')

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 用%%来表示一个%
print 'Hi, %s, you have $%d.' % ('Michael', 1000000)