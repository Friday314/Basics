class Base:
    def test(self):
        print("Base")


class A(Base):
    def test(self):
        print("test1")


class B(Base):
    def test(self):
        print("test2")


class C(A, B):
    pass


c = C()
c.test()

"""
如果多继承，多个父类中有同名的方法
类名.__mro__ 方法决定调用一个方法的时候，搜索的顺序，
如果在某个类中找到了发放，那么就停止搜索
"""
print(C.__mro__)
