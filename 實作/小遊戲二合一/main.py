import tkinter as tk
import random

inpNum = 0
game_choose = 0
min = 0
max = 0
ans = 0
ans1 = 0
ans2 = 0
ans3 = 0
ans4 = 0

window = tk.Tk()
window.title('小遊戲三合一')
window.geometry("360x120")

first_frame = tk.Frame(window)
lbl_name = tk.Label(first_frame, text="請選擇一個遊戲")
lbl_name.pack(side=tk.LEFT)
first_frame.pack()

top_frame = tk.Frame(window)
btn_guess = tk.Button(top_frame, text="終極密碼",
                      command=lambda: call_guess())
btn_guess.pack(side=tk.LEFT)
btn_numdle = tk.Button(top_frame, text="1A2B",
                       command=lambda: call_numdle())
btn_numdle.pack(side=tk.LEFT)
top_frame.pack(side=tk.TOP)

game_frame = tk.Frame(window)
lbl_game = tk.Label(game_frame, text="")
lbl_game.pack()
game_frame.pack()

mid_frame = tk.Frame(window)
ent_number = tk.Entry(mid_frame)
btn_number = tk.Button(mid_frame, text="送出", command=lambda: setNumber())
ent_number.pack()
btn_number.pack()
ent_number.config(state=tk.DISABLED)
btn_number.config(state=tk.DISABLED)
mid_frame.pack()

down_frame = tk.Frame(window)
lbl_name = tk.Label(down_frame, text="")
lbl_name.pack()
down_frame.pack(side=tk.TOP)


def call_guess():
    global game_choose, min, max, ans
    game_choose = 1
    ans = random.randint(1, 100)
    lbl_game["text"] = "來猜數字吧，範圍在 1~100"
    min = 1
    max = 100
    ent_number.config(state=tk.NORMAL)
    btn_number.config(state=tk.NORMAL)


def call_numdle():
    global game_choose, ans1, ans2, ans3, ans4
    game_choose = 2
    lbl_game["text"] = "來猜1A2B吧"
    ans1 = random.randint(0, 9)
    ans2 = random.randint(0, 9)
    ans3 = random.randint(0, 9)
    ans4 = random.randint(0, 9)
    ent_number.config(state=tk.NORMAL)
    btn_number.config(state=tk.NORMAL)


def setNumber():
    global inpNum, max, min, ans, ans1, ans2, ans3, ans4
    if len(ent_number.get()) < 1:
        tk.messagebox.showerror(
            title="ERROR!!!", message="要記得輸入數字喔!"
        )
    else:
        inpNum = int(ent_number.get())

    if game_choose == 1:
        if inpNum == ans:
            lbl_game["text"] = "你贏了!!"
            ent_number.config(state=tk.DISABLED)
            btn_number.config(state=tk.DISABLED)
        elif inpNum > ans:
            max = inpNum
            lbl_game["text"] = "範圍在", min, "~", max
        else:
            min = inpNum
            lbl_game["text"] = "範圍在", min, "~", max
    elif game_choose == 2:
        a = 0
        b = 0
        inp1 = (inpNum - inpNum % 1000)//1000
        inp2 = (inpNum % 1000 - inpNum % 100)//100
        inp3 = (inpNum % 100 - inpNum % 10)//10
        inp4 = inpNum % 10

        if inp1 == ans1:
            a += 1
        elif inp1 == ans2 or inp1 == ans3 or inp1 == ans4:
            b += 1
        if inp2 == ans2:
            a += 1
        elif inp2 == ans1 or inp2 == ans3 or inp2 == ans4:
            b += 1
        if inp3 == ans3:
            a += 1
        elif inp3 == ans1 or inp3 == ans2 or inp3 == ans4:
            b += 1
        if inp4 == ans4:
            a += 1
        elif inp4 == ans2 or inp4 == ans3 or inp4 == ans1:
            b += 1
        if a == 4:
            lbl_game["text"] = "你贏了!!"
            ent_number.config(state=tk.DISABLED)
            btn_number.config(state=tk.DISABLED)
        else:
            lbl_game["text"] = a, "A", b, "B"


window.mainloop()
