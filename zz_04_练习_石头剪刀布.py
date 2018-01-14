
import random


def rock_paper_scissors():

    """
    石头剪刀布游戏
    """

    while True:

        ran = random.randint(0, 2)

        number = int(input("请输入：剪刀(0)  石头(1)  布(2)："))

        if number not in range(0, 3):
            print(ran)
            print("输入错误，请重新输入！")

        elif ran == 0 and number == 2:
            print(ran)
            print("输了，不要走，决战到天亮！")

        elif ran == 1 and number == 0:
            print(ran)
            print("输了，不要走，决战到天亮！")

        elif ran == 2 and number == 0:
            print(ran)
            print("输了，不要走，决战到天亮！")

        elif ran == number:
            print(ran)
            print("平手平手，我们继续！")

        else:
            print(ran)
            print("恭喜你！取得胜利！")


rock_paper_scissors()
