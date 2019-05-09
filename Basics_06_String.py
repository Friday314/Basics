#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2019/5/8 15:51
# @Author     : 张正
# @Email       : zhangzheng@email.com
# @Site         :
# @File          : Basics_04_运算符与表达式.py
# @Software  : PyCharm


# String相关

_str = "Python is My Love"
print("_str 原文本：%s" % _str)

# split() 通过给定的字符，将字符串分割为一个列表
print("split()方法：", end="")
print(_str.split(" "))

# replace() 类似文本中的替换查找，将给定的字符替换成另外一个字符
print("replace()方法：", end="")
print(_str.replace(" ", "_"))


print("\t")


__str = "  **  Python is My Love  **  "
print("_str 原文本：%s" % _str)

# strip() 返回除去字符串两边的空格，不包含字符串中的空格。也可以指定需要除去字符
print("strip()方法：", end="")
print(__str.strip())
print("strip()方法：", end="")
print(__str.strip(" *"))


# format() 字符串格式化符，通过预留的 {} 占位符，向占位符添加字符串。类似填空题
_name = "{} San".format("Zhang")
print("format()方法：", end="")
print(_name)


"""

占位符         转换
%c          字符
%s          通过str()字符串转换来格式化
%i          有符号十进制整数
%d          有符号十进制整数
%u          无符号十进制整数
%o          八进制整数
%x          十六进制整数(小写字母)
%X          十六进制整数(大写整数)
%e          索引符号(小写‘e’)
%E          索引符号(大写‘E’)
%f          浮点实数
%g          %f和%e的简写
%G          %f和%E的简写

"""

myStr = "    Hello \n Worle    "

# .find()   根据字符，找到返回下标，找不到返回-1
# .rfind()  从左边开始查找

print(myStr.find("H"))

# .index()  根据字符，找到返回下标，找不到就报错
# .rindex() 从左边开始查找

print(myStr.index("e"))

# .count()  查找字符出现的次数
print(myStr.count("o"))

# .replace() 替换
# .replace("原字符", "替换的字符", 替换的次数(可选))
print(myStr.replace("Worle", "Word"))

# .split()  切割，返回列表
print(myStr.split(" "))

# .splitlines() 根据换行符切割
print(myStr.splitlines())

# .partition()  分割，返回元祖
# .rpartition() 从右边开始查找
print(myStr.partition("o"))

# .capitalize() 字符串首字母大写
print(myStr.capitalize())

# .title()  字符串每个单词的首字母大写
print(myStr.title())

# .startswith() 判断以什么开头
print(myStr.startswith("W"))

# .endswith()   判断以什么结尾
print(myStr.endswith("e"))

# .lower()  全部小写
print(myStr.lower())

# .upper()  全部大写
print(myStr.upper())

'''
# .rjust()  右对齐
print(myStr.rjust())

# .ljust()  左对其
print(myStr)

# .center() 剧中
print(myStr.center())
'''

# .rstrip() 去右空格
print(myStr.rstrip())

# .lstrip() 去左空格
print(myStr.lstrip())

# .strip()  去左右空格
print(myStr.strip())

# .isalnum()    判断字符串是不是纯字母
print(myStr.isalnum())

# .isdigit()    判断字符串是不是纯数字
print(myStr.isdigit())

# .isalnum()    判断字符串是不是字符与数字的组合
print(myStr.isalnum())

names = ["张三", "李四", "王五"]

a = "——"

# .join() 通过一个字符把列表组合成成字符串
print(a.join(names))
