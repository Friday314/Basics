#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2019/5/8 15:51
# @Author     : 张正
# @Email       : zhangzheng@email.com
# @Site         :
# @File          : Basics_04_运算符与表达式.py
# @Software  : PyCharm


"""

while 条件:
    循环体

手动死循环
while True:
    循环体

"""

_i = 1

while _i <= 10:
    print(_i)
    _i += 1


"""

for 循环

for item in iterable:
    do
    
item        表示元素
iterable    是集合

"""
for _i in range(1, 11):
    print(_i)


names = ["xiaoming", "wangwu", "peter"]
ages = [22, 15, 19]

# 多重循环，通过zip
for name, age in zip(names, ages):
    print(name, age)


urls = ["www.baidu.com/pdf{}".format(number)
        for number in range(1, 11)]

for url in urls:
    print(url)


# 练习输出打印矩形

def _print(number):

    _i = 1

    while _i <= number:

        print("*" * _i)

        _i += 1


_print(10)


# 输出打印99乘法表

_i = 1

while _i <= 9:

    _j = 1

    while _j <= _i:

        print("%d * %d = %d\t" % (_j, _i, _i * _j), end="")

        _j += 1

    print("")

    _i += 1
