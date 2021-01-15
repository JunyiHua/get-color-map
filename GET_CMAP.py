import wx
from tkinter import *
import tkinter.filedialog
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

import get_CM

class GET_CM(wx.Frame): #框架
    def __init__(self, *args, **kw):  # 确保调用父类的__init__
        super(GET_CM, self).__init__(*args, **kw)
        pnl = wx.Panel(self)  # 在框架中创建一个面板
        #采用图形背景
        image_file = 'backiee-180279.jpg'
        to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).Scale(960, 540).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))
        #窗口图标
        icon_file = wx.EmptyIcon()
        icon_file.LoadFile("faviconcm.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon_file)
        #托盘图标

        #透明背景
        self.SetTransparent(200)
        #纯色背景
        pnl.SetBackgroundColour('BLACK')#CYAN
        #st = wx.StaticText(pnl, label="Welcome to the report of CFD")  # 放一些加粗字体在面板上
        #font = st.GetFont()
        #font.PointSize += 10
        #font = font.Bold()
        #st.SetFont(font)
        sizer = wx.BoxSizer(wx.VERTICAL)  # 并创建一个sizer来管理子窗口小部件的布局
        #sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)
        self.makeMenuBar()  # 创建一个菜单栏

        #self.panel = FigureCanvas(self, -1, Figure(figsize = (4,3)))   
        #axes = self.panel.figure.gca()   
        #axes.cla()   
        #axes.plot([1,2,3],[1,2,3])   
        #self.panel.draw()
 
        self.CreateStatusBar()
        self.SetStatusText("北航17375248华浚亦")

 
    def makeMenuBar(self):
        """
        菜单栏由菜单组成，菜单由菜单项组成。
        此方法构建一组菜单并绑定要调用的处理程序
        选择菜单项时。
        """
        startMenu = wx.Menu()  # 使用Hello和Exit项创建一个文件菜单
        # “\ t...”语法定义了一个也触发的加速键
        # 同一事件
        helloItem = startMenu.Append(-1, "&Hello...\tCtrl-H", "这个程序的用处就是通过你给出的图片提取\n并得到一个依照冷暖程度排序的色值表")
        startMenu.AppendSeparator()
        # 使用库存ID时，不需要指定菜单项
        # 标签
        exitItem = startMenu.Append(wx.ID_EXIT)
 
        # 现在是关于项目的帮助菜单
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)
 
        # 制作菜单栏并为其添加两个菜单。'＆'定义
        # 下一个字母是菜单项的“助记符”。在
        # 支持它的平台那些字母加下划线并且可以
        # 从键盘触发。

        openMenu = wx.Menu()
        pictureITEM = openMenu.Append(-1, "&picture", "打开文件")


        menuBar = wx.MenuBar()
        menuBar.Append(startMenu, "&Start")
        menuBar.Append(openMenu, "&Open")
        menuBar.Append(helpMenu, "&Help")
        
 
        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)
 
        # 最后，将处理函数与EVT_MENU事件关联起来
        # 每个菜单项。这意味着当该菜单项是
        # activated然后将调用相关的处理函数。
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.PictureOpen, pictureITEM)
 
    def OnExit(self, event):
        """退出此程序"""
        self.Close(True)
 
 
    def OnHello(self, event):
        wx.MessageBox("Hello again from CFD_Report")
 
 
    def OnAbout(self, event):
        wx.MessageBox("This is a program to help showing visual CFD report",
                      "About CFD_Report",
                      wx.OK|wx.ICON_INFORMATION)
    
    def PictureOpen(self, event):
        Tk().withdraw()
        path = tkinter.filedialog.askopenfilename()
        get_CM.get_cmap(path)
        snsimage_file = (r'C:/Users/hx893/Desktop/get_cmap.png')
        snspng = wx.Image(snsimage_file, wx.BITMAP_TYPE_PNG).Scale(1000,600).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, snspng, (0, 0))

 

if __name__ == '__main__':
    # 运行此模块（未导入）然后创建应用程序，
    # frame，显示它，然后启动事件循环。
    app = wx.App()
    frm = GET_CM(None, -1, title = '获取色值表谱', size = (1000,600))
    frm.Show()
    app.MainLoop()
