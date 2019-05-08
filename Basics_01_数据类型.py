#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2019/5/8 13:45
# @Author     : 张正
# @Email       : zhangzheng@email.com
# @Site         :
# @File          : Basics_01_数据类型.py
# @Software  : PyCharm


# 导入,数学相关库
import math
# 随机数库
import random

'''

                                            int(有符号整数)

                                            long(长整型【也可以代表八进制和十六进制】)
Number (数字)
                                            float(浮点型)

                                            complex(复数)


                                            True
布尔类型
                                            False


String (字符串类型)


List (列表)


Tuple (元组)


Dictionary (字典)

None (空值)

'''

_number = 100

_str = "Hello Word"

_bool = True

_list = [1, 2, 3, 4, 5]

_tup = (1, 2, 3, 4, 5)

_dict = {"Name": "ZhangSan",
         "Age": 18}

# type() 输出变量的数据类型

print(type(_number))
print(_number)

print("----------------")

print(type(_str))
print(_str)

print("----------------")

print(type(_bool))
print(_bool)

print("----------------")

print(type(_list))
print(_list)

print("----------------")

print(type(_tup))
print(_tup)

print("----------------")

print(type(_dict))
print(_dict)

print("----------------")

# 返回数字的绝对值 abs
Number = 10
print(abs(Number))

# 返回给定参数的最大值 max
print(max(9, 3, 46, 1884, 35, 32843, 321564, 3212))

# 返回给定参数的最小值 min
print(min(9, 3, 46, 1884, 35, 32843, 321564, 3212))

# 求X的Y次方 pow
print(pow(2, 5))

# 四舍五入,或取小数位 round
print(round(3.456))
print(round(3.556))
print(round(3.456, 1))
print(round(3.456, 2))

# 向上取整
print(math.ceil(18.1))
print(math.ceil(18.9))
# 向下取整
print(math.floor(18.1))
print(math.floor(18.9))

# 返回整数部分与小数部分
print(math.modf(22.3))

# 开方
print(math.sqrt(16))

# 随机数

# 随机输出列表中的数值
print(random.choice([1, 2, 3, 9, 5, 4, 6, 7, 4, 4, 5, 6, 7]))

# 产生一个1-100之间的随机数
rand = random.choice(range(100)) + 1
print(rand)

