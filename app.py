from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("ラベル作成")
root.geometry("300x300")

list = ["上着","ズボン","帽子"]
ttk.Label(frm,text="デザインを選択").grid(column=1,row=0)
ttk.Combobox(frm,height=3 ,values=list).grid(column=1,row=1)
ttk.Label(frm, text="ファイルをアップロードしてください").grid(column=1, row=2)
ttk.Button(frm,text="ファイル").grid(column=1,row=3)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)
root.mainloop()