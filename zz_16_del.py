class Dog:
    def __del__(self):
        print("______Over_____")


dog = Dog()

dog2 = dog

# 删除，并非删除对象，只是删除对象的引用
# del dog
# del dog2


# 导入库
import sys

# sys.getrefcount(dog) 测量对象的引用计数
# 引用计数 - 1，就是实际的引用计数。
# 如果对象引用计数为零，则函数报错
i = sys.getrefcount(dog)

print(i)
