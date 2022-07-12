import tkinter as tk
import socket
import threading
from time import sleep
import random

window = tk.Tk()
window.title("終極密碼Server")  # 視窗

topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Start", command=lambda: start_server())
btnStart.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))  # 設定開啟伺服器的按鈕

middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame, text="Address: X.X.X.X")
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text="Port:XXXX")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))  # 顯示伺服器資訊

clientFrame = tk.Frame(window)
lblLine = tk.Label(clientFrame, text="**********Client List**********").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientFrame, height=10, width=30)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(
    yscrollcommand=scrollBar.set,
    background="#F4F6F7",
    highlightbackground="grey",
    state="disabled",
)
clientFrame.pack(side=tk.BOTTOM, pady=(5, 10))  # 顯示連線玩家的名字

server = None
client_name = " "
clients = []  # 連線玩家
client_name_list = []  # 玩家姓名
player_data = []
ansstr = ""
HOST_ADDR = "127.0.0.1"  # local address
HOST_PORT = 8080  # local port


def start_server():
    global server, HOST_ADDR, HOST_PORT, answer, ansstr
    btnStart.config(state=tk.DISABLED)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.AF_INET)  # 用ipv4
    print(socket.SOCK_STREAM)  # 用TCP

    server.bind((HOST_ADDR, HOST_PORT))  # bind addr and port
    server.listen(5)  # listen for client

    answer = random.randint(1, 100)  # 決定答案
    ansstr = str(answer)
    print(ansstr)

    threading._start_new_thread(accClients, (server, " "))

    lblHost["text"] = "Address: " + HOST_ADDR
    lblPort["text"] = "Port: " + str(HOST_PORT)


def accClients(sv, y):
    while True:
        if len(clients) < 2:
            client, addr = sv.accept()
            clients.append(client)
            print(client)

            threading._start_new_thread(msgSend, (client, addr))
            # 玩家最多兩個人


def msgSend(client_connection, client_ip_addr):
    global server, client_name, clients, player_data, answer, ansstr

    # send welcome message to client
    client_name = client_connection.recv(4096).decode()
    print(client_name)
    print("test")

    if len(clients) < 2:
        client_connection.send("welcome1".encode())
    else:
        client_connection.send("welcome2".encode())

    client_name_list.append(client_name)
    update_client(client_name_list)  # 更新連線玩家

    if len(clients) > 1:
        sleep(1)

        # 送出對手名字
        clients[0].send(("opponent_name$" + client_name_list[1]).encode())
        clients[1].send(("opponent_name$" + client_name_list[0]).encode())
        # 送出答案
        clients[0].send(("answer$" + ansstr).encode())
        clients[1].send(("answer$" + ansstr).encode())

    while True:
        data = client_connection.recv(4096).decode()
        if not data:
            break

        number_choose = data[6: len(data)]
        print(number_choose)
        msg = {"choose": number_choose, "socket": client_connection}
        player_data.append(msg)
        dataToSend = "$opponent_choose" + player_data[0].get("choose")
        if player_data[0].get("socket") == clients[0]:
            clients[1].send(dataToSend.encode())
        else:
            clients[0].send(dataToSend.encode())
        player_data = []
        if int(number_choose) == answer:
            break

    idx = get_client_index(clients, client_connection)
    del client_name_list[idx]
    del clients[idx]
    client_connection.close()  # client 斷線

    update_client(client_name_list)  # 更新連線玩家


def get_client_index(client_list, current_client):  # 回傳現在玩家的編號
    idx = 0
    for conns in client_list:
        if conns == current_client:
            break
        idx = idx + 1

    return idx


def update_client(name_list):  # 更新連線玩家
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete("1.0", tk.END)

    for c in name_list:
        tkDisplay.insert(tk.END, c + "\n")
    tkDisplay.config(state=tk.DISABLED)


window.mainloop()
