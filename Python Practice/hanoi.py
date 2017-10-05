# -*- coding: UTF-8 -*-

def move(n, a, b, c):
    if n == 1:
        print(a + '-->' + c)
        return
    move(n-1, a, c, b)
    move(n, a, b, c)
    move(n-1, b, a, c)
