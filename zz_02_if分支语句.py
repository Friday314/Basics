"""
if 用来完成判断

if 条件:
    条件成立的时候，做的事情
"""

age = 19

if age >= 18:
    print("可以去网吧嗨皮了")
else:
    print("回家睡大觉吧")


"""
功能升级版

if 条件:
    条件成立的时候，做的事情
else:
    条件不成立的时候，做的事情
"""

# int(input("请输入你的年龄：")) 数据类型转换 Str -> Int
age = int(input("请输入你的年龄："))

if age >= 18:
    print("你可以去网吧嗨皮了！")
else:
    print("你还是回家睡大觉吧！")
