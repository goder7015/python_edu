from cgitb import text
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import socket
from time import sleep
import threading

###############################設定視窗與變數初始化################################
window_main = tk.Tk()
window_main.title("終極密碼Client")
your_name = ""
opponent_name = ""
your_number = ""
opponent_number = ""
minN = 1
maxN = 100
answer = 0
inputN = 0
turn = 0

client = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 8080  # 設定 ADDR 和 PORT

top_welcome_frame = tk.Frame(window_main)
lbl_name = tk.Label(top_welcome_frame, text="Name:")
lbl_name.pack(side=tk.LEFT)
ent_name = tk.Entry(top_welcome_frame)
ent_name.pack(side=tk.LEFT)
btn_connect = tk.Button(top_welcome_frame, text="Connect",
                        command=lambda: connect())
btn_connect.pack(side=tk.LEFT)
top_welcome_frame.pack(side=tk.TOP)

top_message_frame = tk.Frame(window_main)
lbl_line = tk.Label(
    top_message_frame,
    text="***********************************************************",
).pack()
lbl_welcome = tk.Label(top_message_frame, text="")
lbl_welcome.pack()
top_message_frame.pack(side=tk.TOP)

top_guess_frame = tk.Frame(window_main)
ent_guess = tk.Entry(top_guess_frame)
ent_guess.pack(side=tk.LEFT)
btn_guess = tk.Button(top_guess_frame, text="Guess",
                      command=lambda: guessing())
btn_guess.pack(side=tk.LEFT)
top_guess_frame.pack_forget()

top_showNum_frame = tk.Frame(window_main)
lbl_range = tk.Label(top_showNum_frame,
                     text="Wait for start...")
lbl_range.pack(side=tk.LEFT)
top_showNum_frame.pack_forget()
###############################設定視窗與變數初始化################################


def connect():  # 連線，別忘了輸入名字
    global your_name
    if len(ent_name.get()) < 1:
        tk.messagebox.showerror(
            title="ERROR!!!", message="You MUST enter your first name <e.g. John>"
        )
    else:
        your_name = ent_name.get()
        connect_to_server(your_name)


def connect_to_server(name):  # connect and send
    global client, HOST_PORT, HOST_ADDR, your_name
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))
        client.send(name.encode())
        print(name)

        # 把連線按鈕關閉
        btn_connect.config(state=tk.DISABLED)
        ent_name.config(state=tk.DISABLED)
        lbl_name.config(state=tk.DISABLED)

        # 利用新的 thread 來接收訊息
        threading._start_new_thread(mainFunc, (client, "m"))
    except Exception as e:
        tk.messagebox.showerror(
            title="ERROR!!!",
            message="Cannot connect to host: "
            + HOST_ADDR
            + " on port: "
            + str(HOST_PORT)
            + " Server may be Unavailable. Try again later",
        )


def guessing():  # 猜數字，會更改數字範圍
    global inputN, minN, maxN, answer, turn
    inputN = ent_guess.get()
    if int(inputN) > int(maxN):
        lbl_range["text"] = "比最大值還大，重新輸入，" + lbl_range["text"]
    elif int(inputN) < int(minN):
        lbl_range["text"] = "比最小值還小，重新輸入，" + lbl_range["text"]
    else:
        if inputN == answer:
            lbl_range["text"] = "You Win, the answer is " + inputN
        elif int(inputN) > int(answer):
            maxN = int(inputN)
            lbl_range["text"] = "Range is from " + \
                str(minN) + " to " + str(maxN)
        else:
            minN = int(inputN)
            lbl_range["text"] = "Range is from " + \
                str(minN) + " to " + str(maxN)

        if client:  # 猜完之後會送出到 server
            dataToSend = "choose" + str(inputN)
            turn = 0
            client.send(dataToSend.encode())
            game()


def mainFunc(sock, m):
    global your_name, opponent_name
    global your_number, opponent_number
    global turn, minN, maxN, answer

    while True:  # 接收資料
        from_server = str(sock.recv(4096).decode())

        if not from_server:
            break

        if from_server.startswith("welcome"):  # 成功連線等待玩家
            if from_server == "welcome1":
                lbl_welcome["text"] = (
                    "Server says: Welcome " + your_name + "! Waiting for player 2"
                )
                print("connect")
                turn = 1
            elif from_server == "welcome2":
                lbl_welcome["text"] = (
                    "Server says: Welcome " + your_name + "! Game will start soon"
                )
                game()
            top_guess_frame.pack(side=tk.TOP)
            top_showNum_frame.pack(side=tk.TOP)

        elif from_server.startswith("opponent_name$"):  # 成功連線取得對手名字
            print(from_server)
            opponent_name = from_server.replace("opponent_name$", "")
            lbl_welcome["text"] = "Opponent: " + opponent_name

        elif from_server.startswith("answer$"):  # 接收解答，並準備開始競賽
            print(from_server)
            answer = from_server.replace("answer$", "")
            lbl_range["text"] = "Range is from " + \
                str(minN) + " to " + str(maxN)
            game()
            lbl_welcome.config(state=tk.DISABLED)

        elif from_server.startswith("$opponent_choose"):
            # get the opponent choice from the server
            opponent_number = from_server.replace("$opponent_choose", "")
            if int(opponent_number) == int(answer):
                lbl_range["text"] = "You Lose, the answer is " + \
                    opponent_number
                turn = 0
                game()
            elif int(opponent_number) > int(answer):
                maxN = int(opponent_number)
                lbl_range["text"] = "Range is from " + \
                    str(minN) + " to " + str(maxN)
            else:
                minN = int(opponent_number)
                lbl_range["text"] = "Range is from " + \
                    str(minN) + " to " + str(maxN)
            turn = 1
            game()

    sock.close()


def game():
    global turn
    print("turn" + str(turn))
    if turn == 1:
        btn_guess.config(state=tk.NORMAL)
        ent_guess.config(state=tk.NORMAL)
    else:
        btn_guess.config(state=tk.DISABLED)
        ent_guess.config(state=tk.DISABLED)


window_main.mainloop()
