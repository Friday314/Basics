'''
异常
'''

# 报错代码
# 没有进行异常操作，代码报错，程序停止运行
# print(5 / 0)

# ZeroDivisionError异常，Python无法按照你的要求做时，就会创建这种对象
try:
    # try代码块内放觉得会有问题的代码
    number = 4 / 2
except ZeroDivisionError:
    # 如果上方的代码出现异常，则运行以下代码，程序继续往下，避免程序崩溃
    print('代码运行错误')
else:
    # 如果try代码快运行成功，无报错。则输出else
    print(number)

print('-' * 30)

filename = 'alice.txt'

# FileNotFoundError异常，这是Python找不到要打开的文件时创建的异常。
try:
    # 让程序读取一个不存在的文件
    # 铁定报错
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print('没有找到' + filename + '文件。')
