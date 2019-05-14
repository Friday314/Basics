#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2019/5/14 15:19
# @Author     : 张正
# @Email       : zhangzheng@email.com
# @Site         :
# @File          : Basics_04_运算符与表达式.py
# @Software  : PyCharm


# 定义一个列表
names = ['zhangsan', 'lisi', 'wangwu']

# 输出查看
print(names)

# 添加列表数据,append()添加的数据只能添加在列表的最后一位
names.append("赵六")
print(names)

# 指定位置添加数据
names.insert(0, 'wangqi')
print(names)

# 合并两个列表
names2 = ['孙悟空','猪八戒','沙师弟']

names.extend(names2)
print(names)

# 删除，pop()，删除列表最后一位
names.pop()
print(names)

# remove(),根据数据删除，假如有重复内容，只会删除一次
names.remove("wangqi")
print(names)

# del 根据下标删除数据
del names[0]
print(names)

# 修改数据，根据下标修改
names[0] = '李四'
print(names)

# 查找数据
if "李四" in names:
    print("找到了")

if 'lisi' not in names:
    print("没有昵")

# 列表切片
print(names[1:3])
print(names[1:])
print(names[:3])