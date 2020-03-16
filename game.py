"""用python设计的第一个游戏"""

temp=input("不妨猜一下心里想的是哪一个数字:")
guess=int(temp)
while guess!=8:
    t=input("猜错了，再猜一次:")
    guess=int(t)
    if (guess==8):
        print("你是小甲鱼的蛔虫吗")
        print("猜中了也没有奖励")
    else:
        print("要不再试一次")


print("游戏结束")
