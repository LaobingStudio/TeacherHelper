from tkinter import *
from random import randint
from tkinter.messagebox import showinfo, askokcancel
from requests import get
from wget import download

version = "Dev0.1.4"


def random():
    if v.get() == 1:
        number = randint(1, 60)
        text = "学号" + str(number) + "号同学，你被抽到了"
        showinfo("提示", text)
    elif v.get() == 2:
        number = randint(1, 50)
        text = str(number) + "号机同学，你被抽到了"
        showinfo("提示", text)
    else:
        text = "我在写代码了!"
        showinfo("提示", text)


def about():
    AboutMe = Toplevel()
    AboutMe.title("关于")
    AboutMe.iconphoto(False, PhotoImage(False, file='data/LaobingStudioLogo.png'))
    msg = Label(AboutMe, text="""
    TeacherHelper
    版本Dev0.1.4
    © LaobingStudio 保留所有权力
    主要编写人员名单(按照贡献程度):
    烧瑚烙饼(laobinghu)
    """)
    msg.grid(row=1, column=2)
    global logo
    logo = PhotoImage(file="data/LaobingStudioLogo.png")
    logoLabel = Label(AboutMe, image=logo)
    logoLabel.grid(column=1, row=1)


def check_update(if_bequiet=0):
    api_url = "https://api.laobinghu.top/studio/query?software=TeacherHelper&type=update"
    latest_ver = get(api_url).text.replace("\"", "")
    if latest_ver == version:
        if not if_bequiet:
            showinfo("LS通用更新检测", "您已是最新版本!")
    else:
        if askokcancel("LS通用更新检测", "检测到新版本{0},是否更新?".format(latest_ver)):
            upgrade_file_url = "https://f004.backblazeb2.com/file/laobinghustatics/prod/TeacherHelper{0}.exe".format(
                latest_ver)
            file = download(upgrade_file_url, out="TeacherHelper.exe", bar=awa)
        else:
            pass


# 主窗口初始化
root = Tk()
root.minsize(120, 160)
root.maxsize(120, 160)
root.title("老师助手")
root.attributes("-toolwindow", 2, '-topmost', 1)

menubar = Menu(root)
menubar.add_command(label="检查更新", command=check_update)
menubar.add_command(label="关于", command=about)
root.config(menu=menubar)

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

if __name__ == "__main__":
    check_update(True)
    mainloop()
