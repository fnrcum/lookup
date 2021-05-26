# -*- coding: utf-8 -*-
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5 import uic
from tools_ui import Ui_MainWindow
import pprint
from time import sleep
import requests


class LookupTool(QMainWindow):

    def __init__(self, app, parent=None):
        super(LookupTool, self).__init__(parent=parent)
        self.app = app
        self.gui_update_in_progress = True
        self.init_UI()

    def init_UI(self):
        # uic.loadUi(uiFile, self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(800, 588)
        self.ui.quit.clicked.connect(self.quit)
        self.setWindowTitle("Lookup Tool")

    def quit(self):
        self.app.instance().quit()

    def execute_lookup(self):
        acct_nbr = self.ui.acctNbr.text()



