"""

Python 中通过open() 函数打开文件

语法
open(name[, mode[, buffering]])

name        文件名，唯一强制参数
mode        模式， 参数的输入
buffering   缓冲

open() 函数能打开文件，文件不存在，也可以创建文件。如需要写入文件，需要添加参数

'r' 读模式
'w' 写模式
'a' 追加模式
'b' 二进制模式（可添加到其他模式中使用）
'+' 读/写模式（可添加到其他模式中使用）

write() 写入
read()  写入
close() 关闭

文件写入，可加入转义字符

"""
# 打开文件
f = open('C:/Users/Administrator/Desktop/Python_One.txt', "w+")

f.write("Hello Word!\n")
f.write("Hello Python")

f.close()

f = open('C:/Users/Administrator/Desktop/Python_One.txt', "r")

print(f.read())

f.close()
