"""
@ Author: 2054435 廖偲宇
@ Date: 2023-04-29
@ Version: 1.0
@ Description: 编译器主程序（调用集成）
"""

from UI_Manager.ui_startup import *
from UI_Manager.ui_main import *


def main():
    c_compiler = QtWidgets.QApplication(sys.argv)  # 创建 QApplication 对象
    c_compiler.processEvents()  # 处理未处理的事件并使应用程序保持响应，避免开屏影响其他

    open_splash = UI_Splash()  # 创建 开屏画面 对象
    open_splash.effect()

    c_compiler_surface = QtWidgets.QMainWindow()
    ui = UI_Main()
    ui.__init_ui__(c_compiler_surface)
    c_compiler_surface.show()
    open_splash.finish(c_compiler_surface)  # 调用 开屏画面 对象的 finish 方法，结束开屏效果
    sys.exit(c_compiler.exec_())


if __name__ == '__main__':
    main()
