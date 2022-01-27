"""废弃
#画布
canvas = tk.Canvas(mian_program, height=200, width=500)#创建画布
image_file = tk.PhotoImage(file='D:\代码\PyProject\数据储存点\logo.png')#加载图片文件
image = canvas.create_image(0,0, anchor='nw', image=image_file)#将图片置于画布上
canvas.grid(row=0,rowspan=1)
"""
 #进入到日记_第一个输入框.insert(0,"剑锋所指，意志所向！")
'''
def 自定义保存():
    var.set("")
'''
'''循环添加菜单(废弃)
for each in ['视图','编辑']:
    菜单.add_command(label=each)
'''
"""废弃
进入到日记_按钮=tk.Button(
    mian_program,
    text="别找了，这儿！\n点我进入",
    command=打开日记
    );
进入到日记_按钮.grid(row=1,column=0);
"""
"""已经弃用
自定保存日记_按钮=tk.Button(
    mian_program,
    text="自定义保存",
    command=自定义保存
)
"""

"""
    从头开始吧!
    准备设计一个GUI来介绍Python，就用最具代表性的名字“Holle World!”
"""
"""准备与预设"""
import time
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox


"""相关函数"""
def 打开日记():
    tkinter.messagebox.showinfo(title='看来你是真的要记', message='Let’s go!');
    mian_program.title("我现在是日记了┗|｀O′|┛ 嗷~~");
    a.grid_forget()
    写日记_输入框.grid(row=1,column=0,ipadx=True,sticky=tk.N+tk.W+tk.E)
   

    保存日记_按钮.grid(row=2,column=0,sticky=tk.N+tk.W)
    var.set('请写在下面')

def 保存(): #实现获取保存的路径;读取用户输入的文字;保存为txt文件;并提示用户
    with open("D:\代码\PyProject\数据储存点\保存路径.txt","r") as 工具人:
        获取路径=工具人.read()
                                                      
    日记内容=写日记_输入框.get('0.0','end')
    时间=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if 获取路径 is not None:
        with open(file=获取路径+"/"+时间+"日记.txt", mode='a+', encoding='utf-8') as filea:
            filea.write(日记内容)
    var.set("保存成功！q(≧▽≦q)")
    time.sleep(2)
    var.set("当然还可以继续写")

def 个人简介():
    个人信息="姓名：李闻焌\n邮箱：1670350532deyerong@gmail.com"
    tkinter.messagebox.showinfo(message=个人信息)

def 选择保存路径():
    global 保存路径
    保存路径=tk.filedialog.askdirectory()
    with open(file="D:\代码\PyProject\数据储存点\保存路径.txt",mode='w+') as 路径文件:
        路径文件.write(str(保存路径))

def 按钮(文本,命令,x,y,ipadx=True,sticky=None):
    global a
    a=tk.Button(mian_program,text=文本,command=命令)
    a.grid(row=x,column=y,ipadx=ipadx,sticky=sticky)
    return a

"""主窗口"""
mian_program=tk.Tk();
mian_program.title("Holle World");
mian_program.geometry("200x200");
var=tk.StringVar()
    

#主菜单
菜单 = tk.Menu(mian_program)

菜单.add_command(label='关于',command=个人简介)

#分菜单
文件菜单下=tk.Menu(菜单)
文件菜单下.add_command(label="更改保存路径",command=选择保存路径)
菜单.add_cascade(label="文件",menu=文件菜单下)
#实现菜单
mian_program['menu']=菜单

""""进入日记的功能的实现"""
var.set("什么？你要写日记，好吧！")
切换到日记_文字显示=tk.Label(
    mian_program,
    textvariable=var,
    background='pink',
    font=(12), 
    );
切换到日记_文字显示.grid(row=0,column=0);

进入到日记=按钮("别找了，这儿！\n点我进入",打开日记,1,0)

保存日记_按钮=tk.Button(
    mian_program,
    text="千万别忘记保存( •̀ ω •́ )y",
    command=保存
);

写日记_输入框=tk.Text(
    mian_program,
    show=None,
    
    height=6,
    width=20
    );  #第一窗口




mian_program.mainloop()
"""后记:
……做了有两三天了，可以说算是勉强完成，
实在是有些生疏，写了不少废代码（都放至到了最上面）
勉强还算可以
还需要练习
    """
print(保存路径)
