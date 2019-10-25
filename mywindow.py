# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mywindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 351, 281))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 321, 211))
        self.listWidget.setObjectName("listWidget")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.RefreshBtn = QtWidgets.QPushButton(self.groupBox)
        self.RefreshBtn.setGeometry(QtCore.QRect(260, 30, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.RefreshBtn.setFont(font)
        self.RefreshBtn.setObjectName("RefreshBtn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(360, 360, 120, 80))
        self.widget.setObjectName("widget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(400, 40, 351, 281))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.LWScripts = QtWidgets.QListWidget(self.groupBox_2)
        self.LWScripts.setGeometry(QtCore.QRect(10, 60, 321, 211))
        self.LWScripts.setObjectName("LWScripts")
        self.CBScripts = QtWidgets.QCheckBox(self.groupBox_2)
        self.CBScripts.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.CBScripts.setObjectName("CBScripts")
        self.LScriptsRoot = QtWidgets.QLabel(self.groupBox_2)
        self.LScriptsRoot.setGeometry(QtCore.QRect(90, 30, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LScriptsRoot.setFont(font)
        self.LScriptsRoot.setText("")
        self.LScriptsRoot.setObjectName("LScriptsRoot")
        self.BtnSelectScripts = QtWidgets.QPushButton(self.groupBox_2)
        self.BtnSelectScripts.setGeometry(QtCore.QRect(210, 0, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.BtnSelectScripts.setFont(font)
        self.BtnSelectScripts.setObjectName("BtnSelectScripts")
        self.BtnLaunch = QtWidgets.QPushButton(self.centralwidget)
        self.BtnLaunch.setGeometry(QtCore.QRect(480, 400, 261, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.BtnLaunch.setFont(font)
        self.BtnLaunch.setObjectName("BtnLaunch")
        self.CBMode = QtWidgets.QComboBox(self.centralwidget)
        self.CBMode.setGeometry(QtCore.QRect(50, 460, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CBMode.setFont(font)
        self.CBMode.setObjectName("CBMode")
        self.CBMode.addItem("")
        self.CBMode.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 340, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.BtnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.BtnConnect.setGeometry(QtCore.QRect(240, 340, 41, 23))
        self.BtnConnect.setObjectName("BtnConnect")
        self.TextAddr = QtWidgets.QLineEdit(self.centralwidget)
        self.TextAddr.setGeometry(QtCore.QRect(40, 370, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TextAddr.setFont(font)
        self.TextAddr.setObjectName("TextAddr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "你曾哥的启动器"))
        self.groupBox.setTitle(_translate("MainWindow", "List of devices attached"))
        self.checkBox.setText(_translate("MainWindow", "全选"))
        self.RefreshBtn.setText(_translate("MainWindow", "刷新adb"))
        self.groupBox_2.setTitle(_translate("MainWindow", "请选择脚本："))
        self.CBScripts.setText(_translate("MainWindow", "全选"))
        self.BtnSelectScripts.setText(_translate("MainWindow", "选取脚本路径"))
        self.BtnLaunch.setText(_translate("MainWindow", "启动"))
        self.CBMode.setItemText(0, _translate("MainWindow", "模式1"))
        self.CBMode.setItemText(1, _translate("MainWindow", "模式2"))
        self.label.setText(_translate("MainWindow", "远程设备连接"))
        self.BtnConnect.setText(_translate("MainWindow", "连接"))
        self.TextAddr.setText(_translate("MainWindow", "adb connect 127.0.0.1:7555"))
