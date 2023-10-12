"""
@ Author: 2054435 廖偲宇
@ Date: 2023-04-29
@ Version: 1.0
@ Description: 编译器界面
"""

import os

import qtawesome
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPalette, QColor, QFont

from ItemSet import *
from Analyzer.Lexical import *
from ObjectCode import *
from Syntactic import *


# @ 类别名：UI_Main
# @ 类别功能：编译器界面类
class UI_Main(object):
    # @ 函数名：__init_ui__
    # @ 函数功能：初始化UI
    def __init_ui__(self, MainWindow):
        # 设置：主窗口对象
        MainWindow.resize(800, 640)  # 设置主窗口的大小为 800x640
        MainWindow.setObjectName("C Compiler")  # 设置主窗口对象名为 "C Compiler"
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明的属性
        self.MainWindow = MainWindow

        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.main_layout.setSpacing(0)

        self.top_widget = QtWidgets.QWidget()  # 创建头部部件
        self.top_widget.setObjectName('top_widget')
        self.top_layout = QtWidgets.QGridLayout()  # 创建头部部件的网格布局层
        self.top_widget.setLayout(self.top_layout)  # 设置头部部件布局为网格
        self.top_layout.setSpacing(0)

        self.bottom_widget = QtWidgets.QWidget()  # 创建头部部件
        self.bottom_widget.setObjectName('bottom_widget')
        self.bottom_layout = QtWidgets.QGridLayout()  # 创建头部部件的网格布局层
        self.bottom_widget.setLayout(self.bottom_layout)  # 设置头部部件布局为网格
        self.bottom_layout.setSpacing(0)

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.left_widget1 = QtWidgets.QWidget()  # 创建左上侧部件
        self.left_widget1.setObjectName('left_widget1')
        self.left_layout1 = QtWidgets.QGridLayout()  # 创建左上侧部件的网格布局层
        self.left_widget1.setLayout(self.left_layout1)  # 设置左上侧部件布局为网格

        self.left_widget2 = QtWidgets.QWidget()  # 创建左中侧部件
        self.left_widget2.setObjectName('left_widget2')
        self.left_layout2 = QtWidgets.QGridLayout()  # 创建左中侧部件的网格布局层
        self.left_widget2.setLayout(self.left_layout2)  # 设置左中侧部件布局为网格

        self.left_widget3 = QtWidgets.QWidget()  # 创建左下侧部件-占位
        self.left_widget3.setObjectName('left_widget3')
        self.left_layout3 = QtWidgets.QGridLayout()  # 创建左下侧部件的网格布局层-占位
        self.left_widget3.setLayout(self.left_layout3)  # 设置左下侧部件布局为网格-占位

        self.left_layout.addWidget(self.left_widget1, 0, 0, 3, 3)  # 左侧部件在第0行第0列，占3行3列
        self.left_layout.addWidget(self.left_widget2, 3, 0, 6, 3)  # 左侧部件在第3行第0列，占6行3列
        self.left_layout.addWidget(self.left_widget3, 9, 0, 2, 3)  # 左侧部件在第9行第0列，占2行3列

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QStackedLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为堆叠

        """
        @ --------------------------------------------------
        @ 集成窗口：ui_code
        @ 窗口功能：提示框 + 代码框 + 编译框
        @ --------------------------------------------------
        """
        # prompt提示框，指示用户写代码
        self.ui_code = QtWidgets.QMainWindow()
        self.ui_code_main_widget = QtWidgets.QWidget()  # 创建UI1窗口主部件
        # 输入代码
        self.prompt_label = QtWidgets.QLabel("        ╭(●`∀′●)╯ 请输入需要编译的代码 ╰(●’◡’●)╮")

        # 设置：代码框
        self.code_box = QtWidgets.QTextEdit()
        self.code_box.setObjectName("code_box")
        # 设置：代码框行号标签
        self.code_index = QtWidgets.QLabel()
        tmp_line_numbers = '\n'.join(str(i) for i in range(1, 26))  # 行号标签（1-25）
        self.code_index.setText(tmp_line_numbers)
        self.code_index.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # 行号标签（右对齐）
        # 设置：代码框+行号标签 组合为1个部件
        code_widget = QtWidgets.QWidget()  # 创建部件
        tmp_box_1 = QHBoxLayout()  # 横向布局
        tmp_box_1.addWidget(self.code_index)  # 加入布局: 行号
        tmp_box_1.addWidget(self.code_box)  # 加入布局: 代码框
        code_widget.setLayout(tmp_box_1)  # 把布局加入部件

        # 设置：一遍编译按钮
        self.Compile_Button = QPushButton()
        self.Compile_Button.setText('compile')
        # font = QFont("黑体")
        self.Compile_Button.setFont(QFont("黑体"))  # 设置：按钮的字体

        palette = self.Compile_Button.palette()
        palette.setColor(QPalette.ButtonText, QColor(247, 244, 251))  # 设置：按钮字体的颜色

        # # 设置按钮的背景颜色
        self.Compile_Button.setStyleSheet(
            '''
                QPushButton { 
                    background-color: rgb(127, 84, 194); 
                    border-radius: 10px;
                }
            '''
        )
        # self.Compile_Button.setStyleSheet("QPushButton { background-color: rgb(127, 84, 194); }")
        self.Compile_Button.setPalette(palette)

        # 所有按钮的布局
        self.total_code_box = QVBoxLayout()
        self.total_code_box.addWidget(self.prompt_label)  # 加入布局：提示框，指示用户写代码
        self.total_code_box.addWidget(code_widget)  # 加入布局：代码框+行号标签
        self.total_code_box.addWidget(self.Compile_Button)  # 加入布局：编译按钮
        self.ui_code_main_widget.setLayout(self.total_code_box)
        self.ui_code.setCentralWidget(self.ui_code_main_widget)  # 设置窗口主部件

        self.ui_code_main_widget.setStyleSheet(
            '''
            QLabel
            {
                color:grey;
                font-size:18px;
                font-family:'黑体';
             }
            '''
        )
        self.ui_code_main_widget.setStyleSheet(
            '''
                background-color:rgb(41,45,62);
                font-size:18px;
                font-family:'黑体';
            '''
        )
        self.code_index.setStyleSheet(
            '''
                color:rgb(71,76,109);
            '''
        )
        self.prompt_label.setStyleSheet(
            '''
                color:rgb(143,150,197);
                background-color:rgb(49,54,74);
            '''
        )
        self.code_box.setStyleSheet(
            '''
                color:rgb(200,240,144);
            '''
        )

        """
        @ --------------------------------------------------
        @ 集成窗口：ui_lexi
        @ 窗口功能：词法分析表格+滚动条
        @ --------------------------------------------------
        """
        self.ui_lexi = QtWidgets.QMainWindow()
        self.ui_lexi_main_widget = QtWidgets.QWidget()  # 创建UI2窗口主部件

        self.table_lexi = QTableWidget()
        self.table_lexi.setColumnCount(4)
        self.table_lexi.setColumnWidth(0, 160)
        self.table_lexi.setColumnWidth(1, 160)
        self.table_lexi.setColumnWidth(2, 160)
        self.table_lexi.setColumnWidth(3, 160)
        self.table_lexi.setRowCount(16)
        self.table_lexi.setHorizontalHeaderLabels(['类型', '值', '行', '列'])
        # 设置：表格的横轴滚动条
        self.table_lexi.horizontalScrollBar().setStyleSheet(
            '''
                QScrollBar{
                    background-color:rgb(41,45,62); 
                    height:10px;
                    }
                QScrollBar::handle{
                    background-color:rgb(93,98,136);
                    border:2px solid transparent; 
                    border-radius:5px;
                }
                QScrollBar::handle:hover{
                    background-color:rgb(95,146,172);
                }
                QScrollBar::sub-line{
                    background-color:transparent;
                }
                QScrollBar::add-line{
                    background-color:transparent;
                }
            '''
        )
        # 设置：表格的纵轴滚动条
        self.table_lexi.verticalScrollBar().setStyleSheet(
            '''
                QScrollBar{
                    background-color:rgb(41,45,62); 
                    width:10px;
                    }
                QScrollBar::handle{
                    background-color:rgb(93,98,136);
                    border:2px solid transparent; 
                    border-radius:5px;
                }
                QScrollBar::handle:hover{
                    background-color:rgb(95,146,172);
                }
                QScrollBar::sub-line{
                    background-color:transparent;
                }
                QScrollBar::add-line{
                    background-color:transparent;
                }
            '''
        )

        self.total_lexi_box = QHBoxLayout()  # 横向布局
        self.total_lexi_box.addWidget(self.table_lexi)  # 把表格加入布局
        self.ui_lexi_main_widget.setLayout(self.total_lexi_box)
        self.ui_lexi.setCentralWidget(self.ui_lexi_main_widget)  # 设置窗口主部件
        self.table_lexi.setFont(QtGui.QFont('黑体', 12))
        # 循环横向设置表头颜色和字体
        for index in range(self.table_lexi.columnCount()):
            headItem = self.table_lexi.horizontalHeaderItem(index)
            headItem.setFont(QtGui.QFont('黑体', 12))
            headItem.setBackground(QtGui.QColor(49, 64, 74))

        self.ui_lexi_main_widget.setStyleSheet(
            '''
                background-color:rgb(41,45,62);
                font-size:18px;
                font-family:'黑体';
            '''
        )
        self.table_lexi.setStyleSheet(
            '''
                color:rgb(186,194,208);
                background-color:rgb(49,54,74);
            '''
        )
        self.table_lexi.horizontalHeader().setStyleSheet(
            '''
                color:rgb(255,88,118);
                background:rgb(49,54,74);
            '''
        )
        self.table_lexi.verticalHeader().setStyleSheet(
            '''
                color:rgb(77,83,118);
            '''
        )

        """
        @ --------------------------------------------------
        @ 集成窗口：ui_syntac
        @ 窗口功能：语法分析表格+滚动条
        @ --------------------------------------------------
        """
        self.ui_syntactic = QtWidgets.QMainWindow()
        self.ui_syntactic_main_widget = QtWidgets.QWidget()  # 创建UI3窗口主部件

        self.table_syntactic = QTableWidget()
        self.table_syntactic.setColumnCount(3)
        self.table_syntactic.setColumnWidth(0, 214)
        self.table_syntactic.setColumnWidth(1, 214)
        self.table_syntactic.setColumnWidth(2, 214)
        self.table_syntactic.setRowCount(16)
        self.table_syntactic.setHorizontalHeaderLabels(['状态栈', '移动栈', '输入栈'])
        # 设置：表格的横轴滚动条
        self.table_syntactic.horizontalScrollBar().setStyleSheet(
            '''
                QScrollBar{
                    background-color:rgb(41,45,62); 
                    height:10px;
                    }
                QScrollBar::handle{
                    background-color:rgb(93,98,136);
                    border:2px solid transparent; 
                    border-radius:5px;
                }
                QScrollBar::handle:hover{
                    background-color:rgb(95,146,172);
                }
                QScrollBar::sub-line{
                    background-color:transparent;
                }
                QScrollBar::add-line{
                    background-color:transparent;
                }
            '''
        )
        # 设置：表格的纵轴滚动条
        self.table_syntactic.verticalScrollBar().setStyleSheet(
            '''
                QScrollBar{
                    background-color:rgb(41,45,62); 
                    width:10px;
                    }
                QScrollBar::handle{
                    background-color:rgb(93,98,136);
                    border:2px solid transparent; 
                    border-radius:5px;
                }
                QScrollBar::handle:hover{
                    background-color:rgb(95,146,172);
                }
                QScrollBar::sub-line{
                    background-color:transparent;
                }
                QScrollBar::add-line{
                    background-color:transparent;
                }
            '''
        )

        self.total_syntactic_box = QHBoxLayout()  # 横向布局
        self.total_syntactic_box.addWidget(self.table_syntactic)  # 把表格加入布局
        self.ui_syntactic_main_widget.setLayout(self.total_syntactic_box)
        self.ui_syntactic.setCentralWidget(self.ui_syntactic_main_widget)  # 设置窗口主部件
        self.table_syntactic.setFont(QtGui.QFont('黑体', 12))
        # 循环横向设置表头颜色和字体
        for index in range(self.table_syntactic.columnCount()):
            headItem = self.table_syntactic.horizontalHeaderItem(index)
            headItem.setFont(QtGui.QFont('黑体', 12))

        self.ui_syntactic_main_widget.setStyleSheet(
            '''
                background-color:rgb(41,45,62);
                font-size:18px;
                font-family:'黑体';
            '''
        )
        self.table_syntactic.setStyleSheet(
            '''
                color:rgb(186,194,208);
                background-color:rgb(49,54,74);
            '''
        )
        self.table_syntactic.horizontalHeader().setStyleSheet(
            '''
                color:rgb(255,88,118);
                background:rgb(49,54,74);
            '''
        )
        self.table_syntactic.verticalHeader().setStyleSheet(
            '''
                color:rgb(77,83,118);
            '''
        )

        """
        @ --------------------------------------------------
        @ 集成窗口：ui_intermediate
        @ 窗口功能：中间代码生成表格+滚动条
        @ --------------------------------------------------
        """
        self.ui_intermediate = QtWidgets.QMainWindow()
        self.ui_intermediate_main_widget = QtWidgets.QWidget()  # 创建UI4窗口主部件

        self.table_intermediate = QTableWidget()
        self.table_intermediate.setColumnCount(4)
        self.table_intermediate.setColumnWidth(0, 160)
        self.table_intermediate.setColumnWidth(1, 160)
        self.table_intermediate.setColumnWidth(2, 160)
        self.table_intermediate.setColumnWidth(3, 160)
        self.table_intermediate.setRowCount(16)
        self.table_intermediate.setHorizontalHeaderLabels(['operation', 'arg1', 'arg2', 'result'])
        # 设置：表格的横轴滚动条
        self.table_intermediate.horizontalScrollBar().setStyleSheet(
            '''
                QScrollBar{
                    background-color:rgb(41,45,62); 
                    height:10px;
                    }
                QScrollBar::handle{
                    background-color:rgb(93,98,136);
                    border:2px solid transparent; 
                    border-radius:5px;
                }
                QScrollBar::handle:hover{
                    background-color:rgb(95,146,172);
                }
                QScrollBar::sub-line{
                    background-color:transparent;
                }
                QScrollBar::add-line{
                    background-color:transparent;
                }
            '''
        )
        # 设置：表格的纵轴滚动条
        self.table_intermediate.verticalScrollBar().setStyleSheet(
            '''
                QScrollBar{
                    background-color:rgb(41,45,62); 
                    width:10px;
                    }
                QScrollBar::handle{
                    background-color:rgb(93,98,136);
                    border:2px solid transparent; 
                    border-radius:5px;
                }
                QScrollBar::handle:hover{
                    background-color:rgb(95,146,172);
                }
                QScrollBar::sub-line{
                    background-color:transparent;
                }
                QScrollBar::add-line{
                    background-color:transparent;
                }
            '''
        )

        self.total_intermediate_box = QHBoxLayout()  # 横向布局
        self.total_intermediate_box.addWidget(self.table_intermediate)  # 把表格加入布局
        self.ui_intermediate_main_widget.setLayout(self.total_intermediate_box)
        self.ui_intermediate.setCentralWidget(self.ui_intermediate_main_widget)  # 设置窗口主部件
        self.table_intermediate.setFont(QtGui.QFont('黑体', 12))
        # 循环横向设置表头颜色和字体
        for index in range(self.table_intermediate.columnCount()):
            headItem = self.table_intermediate.horizontalHeaderItem(index)
            headItem.setFont(QtGui.QFont('黑体', 12))

        self.ui_intermediate_main_widget.setStyleSheet(
            '''
                background-color:rgb(41,45,62);
                font-size:18px;
                font-family:'黑体';
            '''
        )
        self.table_intermediate.setStyleSheet(
            '''
                color:rgb(186,194,208);
                background-color:rgb(49,54,74);
            '''
        )
        self.table_intermediate.horizontalHeader().setStyleSheet(
            '''
                color:rgb(255,88,118);
                background:rgb(49,54,74);
            '''
        )
        self.table_intermediate.verticalHeader().setStyleSheet(
            '''
                color:rgb(77,83,118);
            '''
        )

        """
        @ --------------------------------------------------
        @ 集成窗口：ui_intermediate
        @ 窗口功能：函数表+滚动条
        @ --------------------------------------------------
        """
        self.ui_function = QtWidgets.QMainWindow()
        self.ui_function_main_widget = QtWidgets.QWidget()  # 创建UI5窗口主部件

        self.table_function = QTableWidget()
        self.table_function.setColumnCount(4)
        self.table_function.setColumnWidth(0, 160)
        self.table_function.setColumnWidth(1, 160)
        self.table_function.setColumnWidth(2, 160)
        self.table_function.setColumnWidth(3, 160)
        self.table_function.setRowCount(16)
        self.table_function.setHorizontalHeaderLabels(['函数的标识符', '返回值类型', '入口处的标签', '形参列表'])
        # 设置：表格的横轴滚动条
        self.table_function.horizontalScrollBar().setStyleSheet(
            '''
                QScrollBar{
                    background-color:rgb(41,45,62); 
                    height:10px;
                    }
                QScrollBar::handle{
                    background-color:rgb(93,98,136);
                    border:2px solid transparent; 
                    border-radius:5px;
                }
                QScrollBar::handle:hover{
                    background-color:rgb(95,146,172);
                }
                QScrollBar::sub-line{
                    background-color:transparent;
                }
                QScrollBar::add-line{
                    background-color:transparent;
                }
            '''
        )
        # 设置：表格的纵轴滚动条
        self.table_function.verticalScrollBar().setStyleSheet(
            '''
                QScrollBar{
                    background-color:rgb(41,45,62); 
                    width:10px;
                    }
                QScrollBar::handle{
                    background-color:rgb(93,98,136);
                    border:2px solid transparent; 
                    border-radius:5px;
                }
                QScrollBar::handle:hover{
                    background-color:rgb(95,146,172);
                }
                QScrollBar::sub-line{
                    background-color:transparent;
                }
                QScrollBar::add-line{
                    background-color:transparent;
                }
            '''
        )

        self.total_function_box = QHBoxLayout()  # 横向布局
        self.total_function_box.addWidget(self.table_function)  # 把表格加入布局
        self.ui_function_main_widget.setLayout(self.total_function_box)
        self.ui_function.setCentralWidget(self.ui_function_main_widget)  # 设置窗口主部件
        self.table_function.setFont(QtGui.QFont('黑体', 12))
        # 循环横向设置表头颜色和字体
        for index in range(self.table_function.columnCount()):
            headItem = self.table_function.horizontalHeaderItem(index)
            headItem.setFont(QtGui.QFont('黑体', 12))

        self.ui_function_main_widget.setStyleSheet(
            '''
                background-color:rgb(41,45,62);
                font-size:18px;
                font-family:'黑体';
            '''
        )
        self.table_function.setStyleSheet(
            '''
                color:rgb(186,194,208);
                background-color:rgb(49,54,74);
            '''
        )
        self.table_function.horizontalHeader().setStyleSheet(
            '''
                color:rgb(255,88,118);
                background:rgb(49,54,74);
            '''
        )
        self.table_function.verticalHeader().setStyleSheet(
            '''
                color:rgb(77,83,118);
            '''
        )

        """
        @ --------------------------------------------------
        @ 集成窗口：ui_intermediate
        @ 窗口功能：符号表+滚动条
        @ --------------------------------------------------
        """
        self.ui_symbol = QtWidgets.QMainWindow()
        self.ui_symbol_main_widget = QtWidgets.QWidget()  # 创建UI6窗口主部件

        self.table_symbol = QTableWidget()
        self.table_symbol.setColumnCount(6)
        self.table_symbol.setRowCount(16)
        self.table_symbol.setHorizontalHeaderLabels(['符号的标识符', '类型', '占用字节数', '内存偏移量', '对应的中间变量', '所在函数'])
        self.table_symbol.horizontalScrollBar().setStyleSheet("QScrollBar{background:transparent; height:10px;}"
                                                              "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
                                                              "QScrollBar::handle:hover{background:gray;}"
                                                              "QScrollBar::sub-line{background:transparent;}"
                                                              "QScrollBar::add-line{background:transparent;}")
        self.table_symbol.verticalScrollBar().setStyleSheet("QScrollBar{background:transparent; width: 10px;}"
                                                            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}"
                                                            "QScrollBar::handle:hover{background:gray;}"
                                                            "QScrollBar::sub-line{background:transparent;}"
                                                            "QScrollBar::add-line{background:transparent;}")
        self.total_symbol_box = QHBoxLayout()  # 横向布局
        self.total_symbol_box.addWidget(self.table_symbol)  # 把表格加入布局
        self.ui_symbol_main_widget.setLayout(self.total_symbol_box)
        self.ui_symbol.setCentralWidget(self.ui_symbol_main_widget)  # 设置窗口主部件
        self.table_symbol.setFont(QtGui.QFont('黑体', 12))
        # 循环横向设置表头颜色和字体
        for index in range(self.table_symbol.columnCount()):
            headItem = self.table_symbol.horizontalHeaderItem(index)
            headItem.setFont(QtGui.QFont('黑体', 12))

        self.ui_symbol_main_widget.setStyleSheet(
            '''
                background-color:rgb(41,45,62);
                font-size:18px;
                font-family:'黑体';
            '''
        )
        self.table_symbol.setStyleSheet(
            '''
                color:rgb(186,194,208);
                background-color:rgb(49,54,74);
            '''
        )
        self.table_symbol.horizontalHeader().setStyleSheet(
            '''
                color:rgb(255,88,118);
                background:rgb(49,54,74);
            '''
        )
        self.table_symbol.verticalHeader().setStyleSheet(
            '''
                color:rgb(77,83,118);
            '''
        )

        """
        @ --------------------------------------------------
        @ 集成窗口：ui_object
        @ 窗口功能：目标代码+滚动条
        @ --------------------------------------------------
        """
        self.ui_object = QtWidgets.QMainWindow()
        self.ui_object_main_widget = QtWidgets.QWidget()  # 创建UI7窗口主部件

        self.total_object_box = QHBoxLayout()
        self.object_code_box = QTextEdit()
        self.total_object_box.addWidget(self.object_code_box)
        self.ui_object_main_widget.setLayout(self.total_object_box)
        self.ui_object.setCentralWidget(self.ui_object_main_widget)  # 设置窗口主部件
        self.object_code_box.setFont(QtGui.QFont('黑体', 12))

        self.ui_object_main_widget.setStyleSheet(
            '''
                background-color:rgb(41,45,62);
                font-size:18px;
                font-family:'黑体';
            '''
        )
        self.code_index.setStyleSheet(
            '''
                color:rgb(71,76,109);
            '''
        )
        self.object_code_box.setStyleSheet(
            '''
                color:rgb(200,240,144);
            '''
        )

        """
        @ --------------------------------------------------
        @ 集成窗口：all
        @ 窗口功能：目标代码+滚动条
        @ --------------------------------------------------
        """

        self.right_layout.addWidget(self.ui_code)
        self.right_layout.addWidget(self.ui_lexi)
        self.right_layout.addWidget(self.ui_syntactic)
        self.right_layout.addWidget(self.ui_intermediate)
        self.right_layout.addWidget(self.ui_function)
        self.right_layout.addWidget(self.ui_symbol)
        self.right_layout.addWidget(self.ui_object)

        self.main_layout.addWidget(self.top_widget, 0, 0, 1, 13)  # 右侧部件在第0行第0列，占1行13列
        self.main_layout.addWidget(self.left_widget, 1, 0, 12, 3)  # 左侧部件在第1行第0列，占12行3列
        self.main_layout.addWidget(self.right_widget, 1, 3, 12, 10)  # 右侧部件在第1行第3列，占12行10列
        self.main_layout.addWidget(self.bottom_widget, 14, 0, 2, 13)  # 底部部件在第12行第0列，占1行13列
        MainWindow.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_layout.setVerticalSpacing(0)
        self.left_layout.setSpacing(0)
        self.left_layout2.setSpacing(0)
        self.left_layout3.setSpacing(0)

        # self.left_out = QtWidgets.QPushButton(qtawesome.icon('fa.sign-out', color='#808080'), "退出")
        # self.left_out.setObjectName('left_out')
        # self.left_out.clicked.connect(MainWindow.close)  # 点击按钮之后关闭窗口

        # self.left_out = QtWidgets.QPushButton(qtawesome.icon('mdi.close', color='rgb(236,106,94)'))
        # 设置：关闭图标
        self.compiler_out = QtWidgets.QPushButton(qtawesome.icon('fa.times-circle', color='#EC6A5E'), "")
        self.compiler_out.setObjectName('compiler_out')
        self.compiler_out.clicked.connect(MainWindow.close)  # 点击按钮之后关闭窗口

        # 设置：放大图标
        self.compiler_full = QtWidgets.QPushButton(qtawesome.icon('fa.plus-circle', color='#61C554'), "")
        self.compiler_full.setObjectName('compiler_full')
        self.compiler_full.clicked.connect(MainWindow.showMaximized)  # 点击按钮之后最大化

        # 设置：缩小图标
        self.compiler_small = QtWidgets.QPushButton(qtawesome.icon('fa.minus-circle', color='#F5BF4F'), "")
        self.compiler_small.setObjectName('compiler_small')
        self.compiler_small.clicked.connect(MainWindow.showMinimized)  # 点击按钮之后最小化

        self.left_username = QtWidgets.QLabel("C Compiler")
        self.left_username.setObjectName('username')

        self.left_close = QtWidgets.QPushButton("")  # 占位
        self.left_visit = QtWidgets.QPushButton("")  # 占位
        self.left_mini = QtWidgets.QPushButton("")  # 占位
        self.zw = QtWidgets.QLabel("")  # 占位
        self.zw2 = QtWidgets.QLabel("")  # 占位

        self.left_label_1 = QtWidgets.QLabel("Admin")
        self.left_label_1.setObjectName('left_label')

        self.left_img_1 = QtWidgets.QLabel("图")
        self.left_img_1.setObjectName('left_img')

        # 按钮
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('mdi.code-greater-than', color='#CCCCCC'),
                                                   "Source Code")
        self.left_button_1.setObjectName('left_button1')
        self.left_button_1.clicked.connect(lambda: self.right_layout.setCurrentIndex(0))
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('mdi.google-analytics', color='#F3C075'),
                                                   "Lexical Analysis")
        self.left_button_2.setObjectName('left_button2')
        self.left_button_2.clicked.connect(lambda: self.right_layout.setCurrentIndex(1))
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('mdi.google-analytics', color='#F3C075'),
                                                   "Syntax Analysis")
        self.left_button_3.setObjectName('left_button3')
        self.left_button_3.clicked.connect(lambda: self.right_layout.setCurrentIndex(2))
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('mdi.checkbox-intermediate', color='#AC4142'),
                                                   "Intermediate Code")
        self.left_button_4.setObjectName('left_button4')
        self.left_button_4.clicked.connect(lambda: self.right_layout.setCurrentIndex(3))
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('mdi.file-table-box-outline', color='#9DC0CE'),
                                                   "Function Table")
        self.left_button_5.setObjectName('left_button5')
        self.left_button_5.clicked.connect(lambda: self.right_layout.setCurrentIndex(4))
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('mdi.file-table-box-outline', color='#9DC0CE'),
                                                   "Symbol Table")
        self.left_button_6.setObjectName('left_button6')
        self.left_button_6.clicked.connect(lambda: self.right_layout.setCurrentIndex(5))
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('mdi.target', color='#DD43C2'), "Target Code")
        self.left_button_7.setObjectName('left_button7')
        self.left_button_7.clicked.connect(lambda: self.right_layout.setCurrentIndex(6))

        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("")  # 设置按钮文本
        self.recommend_button_1.setStyleSheet("font: 14pt \"隶书\";")  # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon(r"./logo.png"))  # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.left_layout1.addWidget(self.recommend_button_1, 0, 0, 1, 1)
        self.left_layout2.addWidget(self.left_button_1, 0, 0, 1, 3)
        self.left_layout2.addWidget(self.left_button_2, 1, 0, 1, 3)
        self.left_layout2.addWidget(self.left_button_3, 2, 0, 1, 3)
        self.left_layout2.addWidget(self.left_button_4, 3, 0, 1, 3)
        self.left_layout2.addWidget(self.left_button_5, 4, 0, 1, 3)
        self.left_layout2.addWidget(self.left_button_6, 5, 0, 1, 3)
        self.left_layout2.addWidget(self.left_button_7, 6, 0, 1, 3)

        self.top_layout.addWidget(self.compiler_out, 0, 2, 1, 1)
        self.top_layout.addWidget(self.compiler_full, 0, 4, 1, 1)
        self.top_layout.addWidget(self.compiler_small, 0, 6, 1, 1)
        self.top_layout.addWidget(self.left_username, 0, 80, 1, 15)

        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout1.setContentsMargins(0, 0, 0, 0)
        self.left_layout2.setContentsMargins(0, 0, 0, 0)
        self.left_layout3.setContentsMargins(0, 0, 0, 0)
        self.right_layout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.Compile_Button.clicked.connect(self.examine_function)

        self.top_widget.setStyleSheet(
            '''
                *{background-color:#292D3E;}
                QLabel
                {
                    color:#F25370;
                    border:none;
                    font-weight:600;
                    font-size:20px;
                    font-family:'黑体';
                 }
                QPushButton
                {
                    color:grey;
                    border:none;
                    font-weight:600;
                    font-size:50px;
                    font-family:'黑体';
                 }
                QWidget#top_widget
                {
                    border-top-left-radius: 10px;
                    border-top-right-radius: 10px;
                }
            '''
        )
        self.bottom_widget.setStyleSheet(
            '''
                *{background-color:#292D3E;}
                QWidget#bottom_widget
                {
                    border-bottom-left-radius: 10px;
                    border-bottom-right-radius: 10px;
                }
            '''
        )
        # 系统标记
        self.left_username.setStyleSheet(
            '''
            QPushButton#username
            { 
                text-align:center;
                padding-left:30px;
                font-size:24px;
            }
        ''')
        self.compiler_out.setStyleSheet(
            '''
            QPushButton#compiler_out
            { 
                text-align:left;
                padding-left:10px;
                color:#fcfcfc;
                font-size:15px;
            }
        ''')
        self.compiler_full.setStyleSheet(
            '''
            QPushButton#compiler_full
            { 
                text-align:left;
                padding-right:10px;
                color:#fcfcfc;
                font-size:15px;
            }
        ''')
        self.compiler_small.setStyleSheet(
            '''
            QPushButton#compiler_small
            { 
                text-align:left;
                padding-right:10px;
                color:#fcfcfc;
                font-size:15px;
            }
        ''')

        self.left_widget.setStyleSheet(
            '''
            QPushButton
            {
                color:#6B7199;
                border:none;
                font-size:15px;
                text-align:left;
                padding-left:30px;
                padding-right:30px;
                padding-top:10px;
                padding-bottom:10px;
                height:30px;
                font-family:'黑体';
            }
            QWidget#left_widget
            {
                color:#6B7199;
                background:#292D3E;
            }
        ''')
        self.left_widget1.setStyleSheet(
            '''
            *{color:grey;}
            QToolButton
            {
                border:none;
                font-weight:600;
                font-size:14px;
                font-family:'隶书';
            }
        ''')
        self.left_widget2.setStyleSheet(
            '''
            QPushButton:hover
            {
                color:#FEFDFE;
                background:#7F54C2;
            }
        ''')
        self.right_widget.setStyleSheet(
            '''
            QWidget#right_widget
            {
                background:red;
            }
        ''')

    # @ 函数名：examine_function
    # @ 函数功能：词法分析、语法分析、语义分析、中间代码、目标代码功能集成测试
    def examine_function(self):
        os.chdir(os.path.dirname(sys.argv[0]))  # 设置工作路径：当前文件目录

        self.lexer = Lexical_Analyzer()  # 词法分析

        self.cfg = CFG()
        self.cfg.tool_read_GrammarFile('./Config/grammar.txt')
        self.cfg.getDotItems()
        self.cfg.calFirstSet()

        self.family = ItemSetSpecificationFamily(self.cfg)
        self.family.buildFamily()
        self.ana = Syntactic_Analyzer(self.lexer, self.cfg, self.family)
        self.ana.getTables()
        self.originCode = self.code_box.toPlainText()
        self.ana.isRecognizable(self.originCode)
        # 语法分析结果
        if self.ana.syntacticRst == False:
            ErrorDialog = QMessageBox.question(self.MainWindow,
                                               "语法分析出错",
                                               self.ana.syntacticErrMsg,
                                               QMessageBox.Yes)
            return
        # 语义分析结果
        elif self.ana.semantic.semanticRst == False:
            ErrorDialog = QMessageBox.question(self.MainWindow,
                                               "语义分析出错",
                                               self.ana.semantic.semanticErrMsg,
                                               QMessageBox.Yes)
            return
        # 语法分析成功后结果
        self.parseRst = self.ana.getParseRst()
        self.ana.semantic.saveMidCodeToFile()
        # 目标代码结果
        self.ocg = ObjectCodeGenerator(self.ana.semantic.middleCode, self.ana.semantic.symbolTable,
                                       self.ana.semantic.funcTable)
        self.ocg.genMips()
        self.mipsText = ''
        for code in self.ocg.mipsCode:
            self.mipsText += code + '\n'

        objCodeFile = open("objCodeFile.txt", "w")
        objCodeFile.write(self.mipsText)
        objCodeFile.close()

        ErrorDialog = QMessageBox.information(self.MainWindow,
                                              "成功",
                                              "生成目标代码成功！",
                                              QMessageBox.Yes)

        # 词法分析结果
        inputProgram = self.code_box.toPlainText()
        self.originCode = inputProgram
        self.tokens = self.lexer.genTokensFromInputBox(inputProgram)
        self.table_lexi.setRowCount(len(self.tokens))
        cnt_row = 0
        for dir in self.tokens:
            cnt_col = 0
            self.table_lexi.setItem(cnt_row, cnt_col, QTableWidgetItem(dir['type']))
            cnt_col = cnt_col + 1
            self.table_lexi.setItem(cnt_row, cnt_col, QTableWidgetItem(dir['data']))
            cnt_col = cnt_col + 1
            self.table_lexi.setItem(cnt_row, cnt_col, QTableWidgetItem(str(dir['row'])))
            cnt_col = cnt_col + 1
            self.table_lexi.setItem(cnt_row, cnt_col, QTableWidgetItem(str(dir['colum'])))
            cnt_row = cnt_row + 1

        # 语法分析结果
        self.table_syntactic.setRowCount(len(self.parseRst))
        cnt_row = 0
        for dir in self.parseRst:
            cnt_col = 0
            li = dir['stateStack']
            s = ""
            for item in li:
                s = s + str(item) + " "
            self.table_syntactic.setItem(cnt_row, cnt_col, QTableWidgetItem(s.strip("->")))
            cnt_col += 1

            li = dir['shiftStr']
            s = ""
            for item in li:
                s = s + str(item['type']) + " "
            self.table_syntactic.setItem(cnt_row, cnt_col, QTableWidgetItem(s))
            cnt_col += 1

            li = dir['inputStr']
            s = ""
            for item in li:
                s = s + str(item['type']) + " "
            self.table_syntactic.setItem(cnt_row, cnt_col, QTableWidgetItem(s))
            cnt_row += 1

        # 中间代码
        self.table_intermediate.setRowCount(len(self.ana.semantic.middleCode))
        cnt_row = 0
        for dir in self.ana.semantic.middleCode:
            cnt_col = 0
            self.table_intermediate.setItem(cnt_row, cnt_col, QTableWidgetItem(dir[cnt_col]))
            cnt_col += 1
            self.table_intermediate.setItem(cnt_row, cnt_col, QTableWidgetItem(dir[cnt_col]))
            cnt_col += 1
            self.table_intermediate.setItem(cnt_row, cnt_col, QTableWidgetItem(dir[cnt_col]))
            cnt_col += 1
            self.table_intermediate.setItem(cnt_row, cnt_col, QTableWidgetItem(dir[cnt_col]))
            cnt_row += 1

        # 函数表
        self.table_function.setRowCount(len(self.ana.semantic.funcTable))
        cnt_row = 0
        for dir in self.ana.semantic.funcTable:
            cnt_col = 0
            self.table_function.setItem(cnt_row, cnt_col, QTableWidgetItem(dir.name))
            cnt_col += 1
            self.table_function.setItem(cnt_row, cnt_col, QTableWidgetItem(dir.type))
            cnt_col += 1
            self.table_function.setItem(cnt_row, cnt_col, QTableWidgetItem(dir.label))
            cnt_col += 1
            self.table_function.setItem(cnt_row, cnt_col, QTableWidgetItem(str(dir.params)))
            cnt_row += 1

        # 符号表
        self.table_symbol.setRowCount(len(self.ana.semantic.symbolTable))
        cnt_row = 0
        for dir in self.ana.semantic.symbolTable:
            cnt_col = 0
            self.table_symbol.setItem(cnt_row, cnt_col, QTableWidgetItem(dir.name))
            cnt_col += 1
            self.table_symbol.setItem(cnt_row, cnt_col, QTableWidgetItem(dir.type))
            cnt_col += 1
            self.table_symbol.setItem(cnt_row, cnt_col, QTableWidgetItem(str(dir.size)))
            cnt_col += 1
            self.table_symbol.setItem(cnt_row, cnt_col, QTableWidgetItem(str(dir.offset)))
            cnt_col += 1
            self.table_symbol.setItem(cnt_row, cnt_col, QTableWidgetItem(dir.place))
            cnt_col += 1
            self.table_symbol.setItem(cnt_row, cnt_col, QTableWidgetItem(dir.function))
            cnt_row += 1

        # 目标代码
        self.object_code_box.setText(self.mipsText)
