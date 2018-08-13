# 创建类
class Cat:
    # 属性
    # 初始化对象
    def __init__(self, new_name="cat", new_age=0):
        self.name = new_name
        self.age = new_age

    def __str__(self):
        # 类似于C#语言的构造方法
        return "猫的名字叫：%s，已经有%s岁了。" % (self.name, self.age)

    # 方法
    # self 谁调用这个类，self就表示谁
    def eat(self):
        print("%s在吃小鱼..." % self.name)

    def drink(self):
        print("%s在喝水..." % self.name)

    def introduce(self):
        print("猫的名字叫：%s，已经有%s岁了。" % (self.name, self.age))


# 创建一个对象
"""
tom = Cat()
tom.name = "汤姆"
tom.age = 44
tom.introduce()
tom.eat()
tom.drink()

print()

lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 19
lanmao.introduce()
lanmao.eat()
lanmao.drink()
"""
cat = Cat()
# cat.introduce()
cat.eat()
cat.drink()
print(cat)

print()

tom = Cat("汤姆", 44)
# tom.introduce()
tom.eat()
tom.drink()
print(tom)

print()

lanmao = Cat("蓝猫", 19)
# lanmao.introduce()
lanmao.eat()
lanmao.drink()
print(lanmao)
