from tkinter import *
from core import random

#主窗口初始化
root = Tk()
root.minsize(100, 130)
root.maxsize(100, 200)


# 很奇怪现阶段模式选择不了所以只能当摆设了呐呐呐(Dev.0.1.1修复)
group1 = LabelFrame(root, text="请选择模式", padx=5, pady=5)
group1.pack(padx=10, pady=5)
MODES = [
    ("学号模式", 1),
    ("机号模式", 2),
    ("名字模式", 3)]

v = IntVar(master=root)
v.set(1)
choice = v.get()

for modes, num in MODES:
    b1 = Radiobutton(group1, text=modes, variable=v, value=num, indicatoron=False)
    b1.pack(anchor=W)


b2 = Button(root, text="抽个人", command=random, width=9, height=1)
b2.pack(anchor=CENTER)

mainloop()
