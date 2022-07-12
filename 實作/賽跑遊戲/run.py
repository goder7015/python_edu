import tkinter as tk
from tkinter import LEFT, messagebox

chr1 = ""
chr2 = ""

len1 = 0
len2 = 0

window = tk.Tk()

window.title('賽跑遊戲')

window.geometry("480x360")

top_frame = tk.Frame(window)
lbl_name1 = tk.Label(top_frame, text="角色輸入1")
lbl_name1.pack(side=tk.LEFT)
ent_name1 = tk.Entry(top_frame)
ent_name1.pack(side=tk.LEFT)
top_frame.pack(side=tk.TOP)

mid_frame = tk.Frame(window)
lbl_name2 = tk.Label(mid_frame, text="角色輸入2")
lbl_name2.pack(side=tk.LEFT)
ent_name2 = tk.Entry(mid_frame)
ent_name2.pack(side=tk.LEFT)
mid_frame.pack(side=tk.TOP)

down_frame = tk.Frame(window)
btn_start = tk.Button(down_frame, text="開始遊戲",
                      command=lambda: game())
btn_start.pack(side=tk.LEFT)
down_frame.pack(side=tk.TOP)

game1_frame = tk.Frame(window)
lbl_game1 = tk.Label(game1_frame, text="", justify=LEFT)
lbl_game1.pack(side=tk.LEFT, anchor="w")
game1_frame.pack(anchor="nw")

game2_frame = tk.Frame(window)
lbl_game2 = tk.Label(game2_frame, text="", justify=LEFT)
lbl_game2.pack(side=tk.LEFT, anchor="w")
game2_frame.pack(anchor="w")


def run1(event):
    global len1
    lbl_game1["text"] = "-" + lbl_game1["text"]
    len1 = len(lbl_game1["text"])
    if len1 > 50:
        lbl_game1["text"] = "You win"
        window.unbind("j")
        window.unbind("f")


def run2(event):
    global len2
    lbl_game2["text"] = "-" + lbl_game2["text"]
    len2 = len(lbl_game2["text"])
    if len2 > 50:
        lbl_game2["text"] = "You win"
        window.unbind("f")
        window.unbind("j")


def game():
    global chr1, chr2
    if len(ent_name1.get()) < 1:
        tk.messagebox.showerror(
            title="ERROR!!!", message="請輸入你的角色(一個字)"
        )
    elif len(ent_name1.get()) > 1:
        tk.messagebox.showerror(
            title="ERROR!!!", message="請輸入你的角色(一個字)"
        )
    elif len(ent_name2.get()) < 1:
        tk.messagebox.showerror(
            title="ERROR!!!", message="請輸入你的角色(一個字)"
        )
    elif len(ent_name2.get()) > 1:
        tk.messagebox.showerror(
            title="ERROR!!!", message="請輸入你的角色(一個字)"
        )
    else:
        chr1 = ent_name1.get()
        chr2 = ent_name2.get()
        start()


def start():
    global len1, len2
    lbl_game1["text"] = chr1
    lbl_game2["text"] = chr2


window.bind("f", run1)
window.bind("j", run2)

window.mainloop()
