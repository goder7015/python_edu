ans = 16


def weather():
    weather = input("現在天氣是晴天、雨天還是陰天呢?\n")
    if weather == '晴天':
        print("天氣真好～")
    elif weather == '陰天':
        print("真希望不要下雨")
    elif weather == '雨天':
        print("天啊，不知道我有沒有帶雨傘")
    else:
        print("你說的不是天氣欸")
        callWeather()


def callWeather():
    weather()


def guess():
    print("從1到20猜個數字吧")
    g = int(input())
    if g == ans:
        return 1
    else:
        return 0


def eat(food):
    if food == "布丁":
        print("QQ彈彈的真好吃")
    elif food == "檸檬茶":
        print("酸酸甜甜的真好喝")
    elif food == "蜂蜜牛奶":
        print("嘿，我有乳糖不耐症，正好給你")
    else:
        callEat()


def callEat():
    eat(input("我的冰箱裡沒有這個，你還想要甚麼嗎?\n"))
