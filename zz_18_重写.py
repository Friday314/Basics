# 创建父类
class Animal:
    # 吃
    def eat(self):
        print("=====吃=====")

    # 喝
    def drink(self):
        print("=====喝=====")

    # 睡
    def sleep(self):
        print("=====睡=====")

    # 跑
    def run(self):
        print("=====跑=====")


# 创建子类，继承父类。
class Dog(Animal):
    # 叫
    def bark(self):
        print("=====叫=====")


# 创建子类，多级继承
class Xiaotian(Dog):
    # 重写父类方法
    def bark(self):
        print("====狂叫====")
        """
        # 第一种：调用被重写的父类方法,此方法的调用，必须添加self
        Dog.bark(self)
        """

        # 第二种：调用被重写的父类方法。此方法不用写父类名称，不用添加self
        super().bark()


"""
wangcai = Dog()
# 子类继承父类方法
wangcai.eat()
# 子类自己的方法
wangcai.bark()
"""

xiaotian = Xiaotian()
xiaotian.bark()
xiaotian.run()
