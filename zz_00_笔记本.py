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
