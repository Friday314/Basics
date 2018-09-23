class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def text1(self):
        print("=====test1=====")

    def __test2(self):
        print("=====test2=====")

    def test3(self):
        self.__test2()
        print(self.__num2)


class B(A):
    pass


b = B()
print(b.num1)
b.text1()
b.test3()

"""
如果调用的是继承的父类中的共有方法
可以在这个共有方法中访问父类中的私有属性和私有方法
但是，如果在子类中实现了一个共有方法，那么
这个方法是不能够调用继承的父类中的私有方法和私有属性
"""
