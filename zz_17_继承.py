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


# 创建子类，继承父类。
class Cat(Animal):
    # 抓老鼠
    def catch(self):
        print("===抓老鼠===")


wangcai = Dog()
# 子类继承父类方法
wangcai.eat()
# 子类自己的方法
wangcai.bark()

tom = Cat()
# 子类继承父类方法
tom.sleep()
# 子类自己的方法
tom.catch()
