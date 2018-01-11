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
