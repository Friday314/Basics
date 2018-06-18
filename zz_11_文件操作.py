"""

Python 中通过open() 函数打开文件

语法
open(name[, mode[, buffering]])

name        文件名，唯一强制参数
mode        模式， 参数的输入
buffering   缓冲

open() 函数能打开文件，文件不存在，也可以创建文件。如需要写入文件，需要添加参数

'r'     读模式
'w'     写模式,如果文件已存在则覆盖。如果文件不存在，创建新文件
'a'     追加模式,如果文件已存在则覆盖。如果文件不存在，创建新文件
'b'     二进制模式（可添加到其他模式中使用）
'+'     读/写模式（可添加到其他模式中使用）

write() 写入
read()  读取
close() 关闭

readline()  按行读取，读一行，返回字符串
readlines() 按行读取，返回列表

文件写入，可加入转义字符

"""

# 打开、创建文件,使用写模式，追加
f = open('txt/Python_One.txt', "a+")

# 写入文件的参数
f.write("Hello Word!\n")
f.write("Hello Python\n")

# 关闭文件
f.close()

f = open('txt/Python_One.txt', "r")

# 读取文件
print(f.read())

# 关闭文件
f.close()


# 练习题，制作文件备份

# 输入文件路径及文件名称
old_file_name = input("请输入文件名：")

# 创建备份文件
# fileNameBak = fileName + ".bak"  # 创建名称不符合规范
number = old_file_name.rfind(".")
new_file_name = old_file_name[0: number] + "[复件]" + old_file_name[number:]

# print(fileNameBak)

# 打开源文件
f_read = open(old_file_name, "r")

# 创建打开备份文件
f_write = open(new_file_name, "w")

"""
# 源文件写入备份文件
有漏洞的代码，如果遇到超大型文件，内存不够用，就会造成数据溢出，代码保存
wr.write(re.read())
"""

# 源文件写入备份文件（升级版）
while True:
    content = f_read.read(1024)     # 一次只读取1024字节

    print(content)

    if len(content) == 0:
        break

    f_write.write(content)

# 关闭备份文件
f_write.close()

# 关闭源文件
f_read.close()
