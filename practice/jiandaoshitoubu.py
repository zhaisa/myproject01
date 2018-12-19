import random
game={1:'石头',2:'剪刀',3:'布'}
count =0
count1=0
while True:
    c = input("请输入你出的id:1:'石头',2:'剪刀',3:'布'")
    if c == "q" or  c =="Q":
        print("您已经退出游戏")
        break
    a=int(c)
    if a>3:
        print("输入序号不对，请重新输入")
        continue
    print("您出的是：{}".format(game[a]))
    a1 = random.randint(1, 3)
    print("系统出的：{}".format(game[a1]))
    if a==1:
        if a1==1:
            print("平局")
            count+=1
        elif a1==2:
            print("您赢了")
            count += 1
            count1 +=1
        elif a1==3:
            print("您输了")
            count += 1
    elif a==2:
        if a1==1:
            print("您输了")
            count += 1
        elif a1==2:
            print("平局")
            count += 1
        elif a1==3:
            print("您赢了")
            count += 1
            count1+=1
    elif a ==3:
        if a1==1:
            print("您赢了")
            count += 1
            count1 += 1
        elif a1==2:
            print("您输了")
            count += 1
        elif a1==3:
            print("平局")
            count += 1

    print("您一共玩了{}局".format(count),"共赢了{}局".format(count1))
