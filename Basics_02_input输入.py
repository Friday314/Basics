#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2019/5/8 13:45
# @Author     : 张正
# @Email       : zhangzheng@email.com
# @Site         :
# @File          : Basics_02_input输入.py
# @Software  : PyCharm


# 扫描控制台,获得用户的输入信息
# input() 输入函数
Number1 = int(input("请输入第一个数字:"))

Number2 = int(input("请输入第二个数字:"))

Temp = Number1 + Number2

print("Number1 + Number2 = ", Temp)

# 查看变量的内存地址 id
print(id(Temp))

# 删除变量 del

del Temp

# 删除变量之后,在调用变量,程序报错
# print(Temp)

