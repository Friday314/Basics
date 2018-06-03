# 定义类
class Bike:

    compose = ['frame', 'wheel', 'pedal']

    # 定义方法
    def use(self):
        print("you are riding")


my_bike = Bike()

you_bike = Bike()

print(my_bike.compose)
print(you_bike.compose)

my_bike.use()


# 定义一个全局变量
wendu = 33


def get_wendu():

    # 定义的局部变量
    # wendu = 30

    """
    如果：全局变量与局部变量重名，在方法中调用时，默认调用局部变量
    """

    # 使用global用来声明一个变量，那么就是对全局变量来进行修改
    global wendu

    wendu = 40

    print(wendu)


get_wendu()
