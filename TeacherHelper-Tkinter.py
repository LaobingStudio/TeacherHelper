from tkinter import *
from random import randint
from tkinter.messagebox import *


def random():
    number = randint(1, 59)
    if v == "PY_VAR1":
        mode = "学号模式"
        text = "学号" + str(number) + "号同学，你被抽到了"
        showinfo("提示", text)
    else:
        mode = "机号模式"
        text = str(number) + "号机同学，你被抽到了"
        showinfo("提示", text)


root = Tk()
root.minsize(100, 125)
root.maxsize(100, 125)
#很奇怪现阶段模式选择不了
#所以只能当摆设了呐呐呐
group1 = LabelFrame(root, text="请选择模式", padx=2, pady=2)
group1.pack(padx=0, pady=0)
MODES = [
    ("学号模式", 1),
    ("机号模式", 2)]
v = IntVar(master=root)
v.set(1)
for modes, num in MODES:
    b1 = Radiobutton(group1, text=modes, variable=v, value=num, indicatoron=False)
    b1.pack(anchor=W)
b2 = Button(root, text="抽个人", command=random)
b2.pack(anchor=CENTER)

mainloop()


