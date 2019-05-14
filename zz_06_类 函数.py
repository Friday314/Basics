# coding=utf-8

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
def text(a, b=10):
    sums = a + b
    print("sum = %d" % sums)


# 调用缺省参数
text(10)

# 不使用缺省参数
text(11, 22)


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


number_2(11, 22, 33, A=11, B=22)


# 拆包
def number_3(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


A = (33, 44, 55)
B = {"name": "laowang", "age": 18}

number_3(11, 22, A, B)

# 拆包调用
number_3(11, 22, *A, **B)

# 匿名函数

# lambda 参数：式子

func = lambda a, b: a + b

number = func(111, 222)

print(number)

# 使用场景
# 列表排序
infos = [{"name": "laowang", "age": 20}, {"name": "lisi", "age": 11}, {"name": "wangwu", "age": 12}]

print(infos)

infos.sort(key=lambda x: x["age"])

print(infos)


# 动态代码语句
def test(a, b, func):
    result = func(a, b)
    print(result)


# 初级版
# test(11, 22, lambda x ,y : x + y)

# 升级版

func_new = input("请输入一个匿名函数：")
# eval() ,转义，字符串去掉冒号
func_new = eval(func_new)

test(1111, 2222, func_new)
