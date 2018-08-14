class Dog:
    def __del__(self):
        print("______Over_____")


dog = Dog()

dog2 = dog

# 删除，并非删除对象，只是删除对象的引用
del dog
del dog2
