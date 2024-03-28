# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModuleSelect.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import gui_scale
from GUI.StyleSheets import get_stylesheet
from functools import partial


class moduleselect(QtWidgets.QMainWindow):
    def __init__(self,parent):
        super(moduleselect,self).__init__(parent)
        self.parent=parent
        self.SetGeometry()
        self.setupUi()
        x = parent.geometry().x() + (parent.geometry().width() -self.__geometry["X"])/2
        y = parent.geometry().y() + parent.geometry().height() / 2
        self.setWindowTitle('模块选择')
        self.setStyleSheet(self.StyleSheet)
        self.pushButton.clicked.connect(self.close)
        self.pushButton.clicked.connect(partial(self.parent.ModuleWindowManager.CreatePartWindown,None))


    def setupUi(self):
        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("ModuleSelect")
        self.widget.resize(self.__geometry["X"], self.__geometry["Y"])
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(self.__Buttongeometry["part"])
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Pic/model-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(self.__Button_width, self.__Button_height))
        self.pushButton.setAutoRepeatDelay(301)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(self.__Buttongeometry["assembly"])
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Pic/assembly-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(self.__Button_width, self.__Button_height))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(self.__Buttongeometry["sheet"])
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Pic/sheet-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(self.__Button_width, self.__Button_height))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(self.__Lable["part"])
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(self.__lable_size)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(self.__Lable["assembly"])
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(self.__lable_size)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(self.__Lable["sheet"])
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(self.__lable_size)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.StyleSheet=('''
                QPushButton {
                "background-color: #4CAF50;"
                border-radius: 50px;
                color: white;
                padding: 10px 20px;
            }
        ''')
        

        self.retranslateUi(self.widget)
        QtCore.QMetaObject.connectSlotsByName(self.widget)
        


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "零件"))
        self.label_2.setText(_translate("Form", "装配"))
        self.label_3.setText(_translate("Form", "钣金"))
    def SetGeometry(self):
        self.__Buttongeometry={}
        self.__Lable={}
        self.__geometry={"X":650,"Y":200}

        self.__Button_width=120
        self.__Button_height=100

        self.__Lable_width=50
        self.__Lable_height=50

        self.__lable_size=15

        button_horizontal=int((self.__geometry["X"]-3*self.__Button_width)/4)
        button_vertical=int((self.__geometry["Y"]-1*self.__Button_width)/2)

        lable_horizontal=button_horizontal+(self.__Button_width-self.__Lable_width)/2
        lable_vertical=5


        self.__Buttongeometry["part"]=QtCore.QRect(button_horizontal, button_vertical, self.__Button_width, self.__Button_height)
        self.__Buttongeometry["assembly"]=QtCore.QRect(2*button_horizontal+self.__Button_width, button_vertical, self.__Button_width, self.__Button_height)
        self.__Buttongeometry["sheet"]=QtCore.QRect(3*button_horizontal+2*self.__Button_width, button_vertical, self.__Button_width, self.__Button_height)

        self.__Lable["part"]=QtCore.QRect(lable_horizontal, button_vertical+self.__Button_height+lable_vertical, self.__Lable_width, self.__Lable_height)
        self.__Lable["assembly"]=QtCore.QRect(1*button_horizontal+self.__Button_width+lable_horizontal, button_vertical+self.__Button_height+lable_vertical, self.__Lable_width, self.__Lable_height)
        self.__Lable["sheet"]=QtCore.QRect(2*button_horizontal+2*self.__Button_width+lable_horizontal, button_vertical+self.__Button_height+lable_vertical, self.__Lable_width, self.__Lable_height)
        self.setFixedSize(self.__geometry["X"], (self.__geometry["Y"]))


    def centerOnScreen(self):
        '''Centers the window on the screen.'''
        resolution = QtWidgets.QApplication.desktop().screenGeometry()
        x = (resolution.width() - self.frameSize().width()) / 2
        y = (resolution.height() - self.frameSize().height()) / 2
        self.move(x, y)