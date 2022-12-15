from tkinter import *
from random import randint
from tkinter.messagebox import showinfo
def random():
    if v.get() == 1:
        mode = "学号模式"
        number = randint(1, 60)
        text = "学号" + str(number) + "号同学，你被抽到了"
        showinfo("提示", text)
    elif v.get() == 2:
        mode = "机号模式"
        number = randint(1, 50)
        text = str(number) + "号机同学，你被抽到了"
        showinfo("提示", text)
    else:
        mode = "名字模式"
        text = "我在写代码了!"
        showinfo("提示", text)

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

for modes, num in MODES:
    b1 = Radiobutton(group1, text=modes, variable=v, value=num, indicatoron=False)
    b1.pack(anchor=W)


b2 = Button(root, text="抽个人", command=random, width=9, height=1)
b2.pack(anchor=CENTER)

mainloop()
