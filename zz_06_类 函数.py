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


# a未赋值，b赋值，表明为缺省参数，调动方法时，如为b赋值，就使用缺省参数。10
def text(a, b = 10):
    sums = a + b
    print("sum = %d" % sums)


# 调用缺省参数
text(10)

# 不使用缺省参数
text(11,22)


# 不定长参数,*args,代表一个元祖。如果方法有多个参数，元祖需要放在最后一个参数
def number(a, b, *args):
    print(a)
    print(b)
    print(args)

    sum = a + b

    for num in args:
        sum += num

    print(sum)


number(1, 2, 3, 4, 5, 6, 7, 8, 9)


# 不定长参数，*表示：可以保存多余的，不定长的参数。**表示：可以保存实参里带有变量名的参数
def number_2(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


number_2(11, 22, 33, A = 11, B = 22)


# 拆包
def number_3(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


A = (33, 44, 55)
B = {"name":"laowang", "age":18}

number_3(11, 22, A, B)

# 拆包调用
number_3(11, 22, *A, **B)