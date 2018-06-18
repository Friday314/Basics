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
