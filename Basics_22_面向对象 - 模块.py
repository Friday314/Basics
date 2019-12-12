'''
1、使用标准库模块

标准库模块：time datetime os ......
'''

'''
2、使用自定义模块
使用imoprt导入一个自写的模块
'''
# 引入一个自定义模块
import sunck

sunck.sayNice()
sunck.sayGood()

# 从一个模块中导入一个指定的部分内容
# 格式：from 模块名 import 指定内容名称 as 自定义名称
from sunck import sayNice as sn

sn()

# 把一个模块中的所有内容全部导入
# 格式：from 模块名 import *
from sunck import *

sayNice()
sayGood()
