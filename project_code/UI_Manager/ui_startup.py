"""
@ Author: 2054435 廖偲宇
@ Date: 2023-04-29
@ Version: 1.0
@ Description: 启动界面
"""

import time

from PyQt5 import QtGui
from PyQt5.QtWidgets import QSplashScreen

# @ 类别名：UI_Splash
# @ 类别功能：开屏图片类
class UI_Splash(QSplashScreen):
    # @ 函数名：__init__
    # @ 函数功能：构造函数
    # @ 参数：self
    def __init__(self):
        # super 调用父类构造函数，设置启动程序窗口图片（开屏）
        super(UI_Splash, self).__init__(QtGui.QPixmap("splash.png"))

    # @ 函数名：effect
    # @ 函数功能：设置动画效果
    # @ 参数：self
    def effect(self):
        # 将窗口初始透明度设置为0
        self.setWindowOpacity(0)
        # 逐渐显示图片
        while True:
            new_opacity = self.windowOpacity() + 0.03  # 将窗口透明度增加0.03
            if new_opacity > 1:  # 如果透明度超过1，退出循环
                break
            self.setWindowOpacity(new_opacity)  # 设置新的窗口透明度
            self.show()  # 显示更新后的启动屏幕
            time.sleep(0.02)  # 等待一小段时间
