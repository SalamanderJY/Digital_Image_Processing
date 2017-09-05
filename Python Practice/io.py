# -*- coding: UTF-8 -*-

print ('hello world')

print ('The quick brown fox', 'jumps over', 'the lazy dog')
# python2的特性就是按需要用括号 应该是 print 'a' 'b'
print ('The quick brown fox', 'jumps over', 'the lazy dog')

print(300)

print(100+200)

print '100 + 200 =', 100 + 200
# Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里。
# name = input()

name = input('please enter your name: ')
print('hello,', name)