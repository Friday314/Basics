class Dog:

    def set_Age(self, new_age):

        if new_age > 0 and new_age <= 100:
            self.age = new_age
        else:
            self.age = 0

    def get_Age(self):
        return self.age

    """
    方法名称前面加双下划线，表示此方法为私有方法
    调用方法：
        使用self调用
    """

    def __test(self):
        print("_____私有方法测试_____")

    def test2(self):
        self.__test()


dog = Dog()
# dog.__test() 私有方法，不能调用
dog.test2()
