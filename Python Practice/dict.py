# -*- coding: UTF-8 -*-

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']

'Thomas' in d
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('Thomas')
d.get('Thomas', -1)

d.pop('Bob')
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s = set([1, 2, 3])
s = set([1, 1, 2, 2, 3, 3])

s.add(4)

s.remove(4)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

s1 & s2

s1 | s2

# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象