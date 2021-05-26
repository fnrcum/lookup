# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 10, 751, 491))
        self.tabWidget.setObjectName("tabWidget")
        self.lookup_tool = QtWidgets.QWidget()
        self.lookup_tool.setObjectName("lookup_tool")
        self.lookupButton = QtWidgets.QPushButton(self.lookup_tool)
        self.lookupButton.setGeometry(QtCore.QRect(370, 40, 131, 41))
        self.lookupButton.setObjectName("lookupButton")
        self.resultArea = QtWidgets.QTextBrowser(self.lookup_tool)
        self.resultArea.setGeometry(QtCore.QRect(20, 140, 311, 311))
        self.resultArea.setObjectName("resultArea")
        self.acctNbr = QtWidgets.QLineEdit(self.lookup_tool)
        self.acctNbr.setGeometry(QtCore.QRect(180, 40, 181, 31))
        self.acctNbr.setObjectName("acctNbr")
        self.requestDataArea = QtWidgets.QTextBrowser(self.lookup_tool)
        self.requestDataArea.setGeometry(QtCore.QRect(350, 140, 381, 311))
        self.requestDataArea.setObjectName("requestDataArea")
        self.resultLbl = QtWidgets.QLabel(self.lookup_tool)
        self.resultLbl.setGeometry(QtCore.QRect(100, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.resultLbl.setFont(font)
        self.resultLbl.setObjectName("resultLbl")
        self.requestLbl = QtWidgets.QLabel(self.lookup_tool)
        self.requestLbl.setGeometry(QtCore.QRect(380, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.requestLbl.setFont(font)
        self.requestLbl.setObjectName("requestLbl")
        self.tabWidget.addTab(self.lookup_tool, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(640, 510, 113, 32))
        self.quit.setObjectName("quit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lookup Tool"))
        self.lookupButton.setText(_translate("MainWindow", "Lookup"))
        self.acctNbr.setText(_translate("MainWindow", "Account Number Here"))
        self.resultLbl.setText(_translate("MainWindow", "Results"))
        self.requestLbl.setText(_translate("MainWindow", "Request data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lookup_tool), _translate("MainWindow", "Lookup Tool"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "nothing_yet"))
        self.quit.setText(_translate("MainWindow", "Quit"))
