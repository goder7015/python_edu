import time
from chatFunc import *

print("哈囉，大家好，我是 Tim 老師的小小聊天機器人")
time.sleep(1)
name = input("能告訴我你的名字嗎?\n")
if name == 'Tim':
    print("哈囉，很高興看到你回來")
else:
    print("嗨，是新朋友～")
time.sleep(1)

print("現在，我想跟你聊聊天氣")
time.sleep(1)
weather()
time.sleep(1)

print("現在，我們來玩個小遊戲")
time.sleep(1)
print("請你輸入一個數字，猜猜看我心裡在想的是多少，有三次機會喔!")
time.sleep(1)

if guess() == 1:
    print("恭喜你答對了")
else:
    print("你還有兩次機會，再猜猜看吧")
    time.sleep(1)
    if guess() == 1:
        print("恭喜你答對了")
    else:
        print("你還有一次機會，再猜猜看吧")
        time.sleep(1)
        if guess() == 1:
            print("恭喜你答對了")
        else:
            print("太可惜了，通通猜錯了 :(")
time.sleep(1)

print("遊戲玩夠了，我們來吃點點心喝點飲料吧")
time.sleep(1)
print("我的冰箱裡有布丁、檸檬茶、以及蜂蜜牛奶，你想要哪個?")
eat(input())

time.sleep(3)
print("很高興今天跟你一起聊天，下次再見～")
