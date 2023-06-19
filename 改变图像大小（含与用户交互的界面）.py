# 这是使用Python Tkinter库和Pillow库创建的小型GUI程序，用于压缩和转换图片格式。
# 程序界面包括一个列表框，用于显示选定的图像文件，以及三个按钮，用于执行压缩和转换操作。

from tkinter import *   #加载全部
from tkinter.filedialog import *
from PIL import Image
from PIL import ImageOps
import os

# info=None  #模拟公共变量，把ui_getdata获取的路径名交给compress使用
info={'path':[]}

def make_app():
    app=Tk()
    Label(text='图片处理').pack()
    Listbox(app,name='lbox',bg='#f2f2f2').pack(fill=BOTH,expand=True)  #属于app的子控件 调用名可以是lbox
    Button(text='click',command=ui_getdata).pack()
    button_compress=Button(text='compress', command=compress)#点击时执行command，定义函数compress
    button_compress.pack()
    tooltip = Tooltip(button_compress, "压缩到桌面文件夹b")# 创建提示文字并绑定到按钮上
    Button(text='convert', command=convert).pack()
    tooltip = Tooltip(button_compress, "png/jpg格式互换到桌面文件夹here")
    app.geometry('300x400')
    return app


def ui_getdata():
    file=askopenfilenames()
    lb=app.children['lbox']  #children返回字典
    info['path']=file
    if info['path']:
        for name in file:
            lb.insert(END,name.split('/')[-1])  #abc.jpg


def compress():
    for f_path in info['path']:
        output='C:/Users/Administrator/Desktop/b'
        if not os.path.exists(output):
            os.makedirs(output)
        name=f_path.split('/')[-1]
        img=Image.open(f_path)
        img.save(output+'/graph_'+name,qualty=60)


def convert():
    for f_path in info['path']:
        output = 'C:/Users/Administrator/Desktop/here'
        if not os.path.exists(output):
            os.makedirs(output)
        name = f_path.split('/')[-1]
        if f_path.split('.')[-1]=='PNG' or f_path.split('.')[-1]=='png':
            PNG_JPG(f_path,output)
        elif f_path.split('.')[-1]=='jpg' or f_path.split('.')[-1]=='JPG':
            JPG_PNG(f_path,output)


def PNG_JPG(f_path,output):
    #img = cv2.imread(PngPath,0) #imread图片的路径中绝对不能含有中文名所以不用
    # print(img.mode, img.size)
    infile =f_path
    outfile = os.path.splitext(infile)[0] + ".jpg"
    filename = os.path.basename(outfile)
    img = Image.open(infile)
    try:
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            # 设置png底色为白色，创建白色画布
            white_image = Image.new('RGB', img.size, 'white')
            white_image.paste(img, mask=a)  #使用原始PNG图像的alpha通道作为掩码
            img = white_image
            img.save(output + "/" + filename)
        else:
            img.convert('RGB')
            img.save(output + "/" + filename)
        return 0
    except Exception as e:
        print("PNG转换JPG 错误", e)


def JPG_PNG(f_path,output): #成功
    img = Image.open(f_path)
    infile = f_path
    outfile = os.path.splitext(infile)[0] + ".png"
    filename = os.path.basename(outfile)
    img = Image.open(infile)
    (w, h) = Image.open(infile).size
    png = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    png.paste(img, (0, 0))
    png.save(output+"/"+filename)
    # c = canvas.Canvas(outfile, pagesize=portrait((w, h)))
    # c.drawImage(infile, 0, 0, w, h)
    # c.showPage()
    # c.save()



# 实现鼠标放在按钮上显示提示文字
# 创建了一个Tooltip类，它接受两个参数：一个是要添加提示文字的控件，另一个是提示文字的文本内容。
# 将鼠标进入和离开事件,绑定到show_tooltip和hide_tooltip方法上。
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tooltip = Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry("+%d+%d" % (x, y))
        Label(self.tooltip, text=self.text, bg="lightyellow", font="Arial 8", relief="solid", bd=1).pack(ipadx=1)

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()

# -*- coding: utf-8 -*-
app=make_app()
app.mainloop()


# #GUI窗口
# # https://v.youku.com/v_show/id_XNDE2NDE5Njg1Mg==.html?spm=a2hbt.13141534.1_2.d1_80&f=52127595
# import tkinter
# root=tkinter.Tk()
# root.title('Tester')  #顶层窗口名称
# root.geometry("500x300+200+20")  #设置窗口大小
# 创建一个标签,文字，背景颜色，字体（颜色，大小），标签的高和宽
# label = tkinter.Label(root,text='输入文字：',font=('宋体',20),bg='black',width=10,height=8)
# label.grid
# #创建按钮
# button = tkinter.Button(root,text='按钮',command='hello')
# button.pack()

# tkinter.mainloop()