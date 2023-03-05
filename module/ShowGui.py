# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from OCC.Display.qtDisplay import qtViewer3d
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import MainGui

from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView,
                             QComboBox, QPushButton, QDockWidget, QListWidget)
from PyQt5.QtGui import QKeySequence as QKSec
from PyQt5.QtGui import QIcon,QBrush
from GUI.RibbonButton import RibbonButton
from GUI.Icons import get_icon
from GUI.RibbonTextbox import RibbonTextbox
from GUI.RibbonWidget import *
from PyQt5.QtCore import  Qt
from module import DisplayManager,ModelTree

class Ui_MainWindow(MainGui.Ui_MainWindow):
    def __init__(self):
        self.setupUi(self)
        self.Displayshape_core=DisplayManager.DisplayManager(self)
        self.modeltree=ModelTree.ModelTree()
        self.setCentralWidget(self.Displayshape_core.canve)

        # -------------------------------------------------------------------------------------右键单击菜单
        self.menuBar = QtWidgets.QMenuBar()
        self.menuBar.setObjectName("menuBar")
        self.Displayshape_core.canve.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Displayshape_core.canve.customContextMenuRequested['QPoint'].connect(self.rightMenuShow)

        # -------------      actions       -----------------
        self._open_action = self.add_action("Open", "open", "Open file", True, self.on_open_file, QKSec.Open)
        self._save_action = self.add_action("Save", "save", "Save file", True, self.on_save, QKSec.Save)
        self._copy_action = self.add_action("Copy", "copy", "Copy selection", True, self.on_copy, QKSec.Copy)
        self._paste_action = self.add_action("Paste", "paste", "Paste from clipboard", True, self.on_paste, QKSec.Paste)
        self._zoom_action = self.add_action("Zoom", "zoom", "Zoom in on document", True, self.on_zoom)
        self._about_action = self.add_action("About", "about", "About QupyRibbon", True, self.on_about)
        self._license_action = self.add_action("License", "license", "Licence for this software", True, self.on_license)

        # -------------      textboxes       -----------------

        self._text_box1 = RibbonTextbox("Text 1", self.on_text_box1_changed, 80)
        self._text_box2 = RibbonTextbox("Text 2", self.on_text_box1_changed, 80)
        self._text_box3 = RibbonTextbox("Text 3", self.on_text_box1_changed, 80)

        # Ribbon

        self._ribbon = RibbonWidget(self)
        self.addToolBar(self._ribbon)
        self.init_ribbon()



        # 界面布局
        # self.items.setWidget(self)
        # self.setCentralWidget(self.stackedWidget)
        # self.items2.setWidget()

        self.items = QDockWidget('组合浏览器', self)  # 新建QDockWidget
        self.addDockWidget(Qt.LeftDockWidgetArea, self.items)  # 在主显示区域右侧显示
        self.items.setMaximumWidth(400)  # 设置最小大小
        self.items.setWidget(self.modeltree.tree)




    def closeEvent(self, close_event):
        pass

    def on_open_file(self):
        pass
        root_dict=self.Displayshape_core.Open_part()
        try:
            self.modeltree.Create_tree_NodeList(root_dict=root_dict)
        except Exception as e:
            print(e)

    def on_save_to_excel(self):
        pass

    def on_save(self):
        pass

    def on_text_box1_changed(self):
        pass

    def on_text_box2_changed(self):
        pass

    def on_text_box3_changed(self):
        pass

    def on_copy(self):
        pass

    def on_paste(self):
        pass

    def on_zoom(self):
        pass

    def on_about(self):
        text = "QupyRibbon\n"
        text += "This program was made by Magnus Jørgensen.\n"
        text += "Copyright © 2016 Magnus Jørgensen"
        QMessageBox().about(self, "About QupyRibbon", text)

    def on_license(self):
        file = open('LICENSE', 'r')
        lic = file.read()
        QMessageBox().information(self, "License", lic)

    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(connection)
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.addAction(action)
        return action

    def init_ribbon(self):
        #------文件选项----------------------------------
        home_tab = self._ribbon.add_ribbon_tab("文件")#table 选项
        file_pane = home_tab.add_ribbon_pane("File")#选项下的菜单
        file_pane.add_ribbon_widget(RibbonButton(self, self._open_action, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self._save_action, True))

        edit_panel = home_tab.add_ribbon_pane("Edit")#选项下的菜单
        edit_panel.add_ribbon_widget(RibbonButton(self, self._copy_action, True))
        edit_panel.add_ribbon_widget(RibbonButton(self, self._paste_action, True))

        grid = edit_panel.add_grid_widget(200)#选项下的菜单
        grid.addWidget(QLabel("Text box 1"), 1, 1)
        grid.addWidget(QLabel("Text box 2"), 2, 1)
        grid.addWidget(QLabel("Text box 3"), 3, 1)
        grid.addWidget(self._text_box1, 1, 2)
        grid.addWidget(self._text_box2, 2, 2)
        grid.addWidget(self._text_box3, 3, 2)

        # ------View选项----------------------------------
        view_panel = home_tab.add_ribbon_pane("View")#选项下的菜单
        view_panel.add_ribbon_widget(RibbonButton(self, self._zoom_action, True))
        home_tab.add_spacer()

        # ------工具----------------------------------
        tool_tab = self._ribbon.add_ribbon_tab("工具")
        tool_panel = tool_tab.add_ribbon_pane("Info")
        tool_panel.add_ribbon_widget(RibbonButton(self, self._about_action, True))
        tool_panel.add_ribbon_widget(RibbonButton(self, self._license_action, True))

        # ------建模----------------------------------
        fix_tab = self._ribbon.add_ribbon_tab("建模")
        fix_panel = fix_tab.add_ribbon_pane("Info")
        fix_panel.add_ribbon_widget(RibbonButton(self, self._about_action, True))
        fix_panel.add_ribbon_widget(RibbonButton(self, self._license_action, True))

        # ------其他----------------------------------
        about_tab = self._ribbon.add_ribbon_tab("其他")
        info_panel = about_tab.add_ribbon_pane("Info")
        info_panel.add_ribbon_widget(RibbonButton(self, self._about_action, True))
        info_panel.add_ribbon_widget(RibbonButton(self, self._license_action, True))

    def rightMenuShow(self):
        try:
            if True:
                rightMenu = QtWidgets.QMenu(self.menuBar)
                self.actionreboot = QtWidgets.QAction(self.canva)
                self.actionreboot.setObjectName("actionreboot")
                self.actionreboot.setText(QtCore.QCoreApplication.translate("MainWindow", "距离测量"))

                self.actionreboot_1 = QtWidgets.QAction(self.canva)
                self.actionreboot_1.setObjectName("actionreboot_1")
                self.actionreboot_1.setText(QtCore.QCoreApplication.translate("MainWindow", "孔径测量"))

                rightMenu.addAction(self.actionreboot)
                rightMenu.addAction(self.actionreboot_1)

                self.actionreboot.triggered.connect(self.Measure_distance_fun)
                self.actionreboot_1.triggered.connect(self.Measure_diameter_fun)

                rightMenu.exec_(QtGui.QCursor.pos())


        except Exception as e:
            print(e)
            pass







