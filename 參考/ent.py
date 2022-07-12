import tkinter as tk


def onOK():
    # 取得輸入文字
    print("Hello, {}.".format(entry.get()))


window = tk.Tk()
window.title('Hello World')
window.geometry("300x100+250+150")

# 標示文字
label = tk.Label(window, text='姓名')
label.pack()

# 輸入欄位
entry = tk.Entry(window,     # 輸入欄位所在視窗
                 width=20)  # 輸入欄位的寬度
entry.pack()

# 按鈕
button = tk.Button(window, text="OK", command=onOK)
button.pack()

window.mainloop()
