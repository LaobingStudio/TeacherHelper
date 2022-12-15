from random import randint
from tkinter.messagebox import showinfo
import gui
def random():
    if gui.choice == 1:
        mode = "学号模式"
        number = randint(1, 60)
        text = "学号" + str(number) + "号同学，你被抽到了"
        showinfo("提示", text)
    elif gui.choice == 2:
        mode = "机号模式"
        number = randint(1, 50)
        text = str(number) + "号机同学，你被抽到了"
        showinfo("提示", text)
    else:
        mode = "名字模式"
        text = "我在写代码了!"
        showinfo("提示", text)