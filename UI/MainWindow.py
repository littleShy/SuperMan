# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5.QtWidgets import QMainWindow

import Ui_Progresses
from Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    progressForm = None
    netClassifyChangedSignal = pyqtSignal(int)
    doTaskTypeChangedSignal = pyqtSignal(int)
    usePlayInterValSignal = pyqtSignal(bool)
    beginDoTaskSignal = pyqtSignal(bool)
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(parent)
        self.initSignalSlot()
        # self.progressForm = QtWidgets.QWidget()
        # ui = Ui_Progresses.Ui_progressForm()
        # ui.setupUi(self.progressForm)
    
    def initSignalSlot(self):

        self.netClassify.currentIndexChanged['int'].connect(self.on_netClassify_currentIndexChanged)
        self.pushButton.clicked['bool'].connect(self.on_doTask_clicked)
        self.checkBox.clicked['bool'].connect(self.on_playInterval_clicked)
        self.doTaskType.currentIndexChanged['int'].connect(self.on_doTaskType_currentIndexChanged)

    @pyqtSlot(int)
    def on_netClassify_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        self.netClassifyChangedSignal.emit(index)

    @pyqtSlot(int)
    def on_doTaskType_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        self.doTaskTypeChangedSignal.emit(index)
    
    @pyqtSlot(bool)
    def on_playInterval_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        self.usePlayInterValSignal.emit(checked)
    
    @pyqtSlot(bool)
    def on_doTask_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        print('on_dotask_clicked! ', checked)
        _translate = QtCore.QCoreApplication.translate
        if not checked:
            self.pushButton.setText(_translate("MainWindow", "停止做任务"))
            self.progressForm.show()
        else:
            self.pushButton.setText(_translate("MainWindow", "开始做任务"))
            self.progressForm.hide()
        self.beginDoTaskSignal.emit(checked)

class UIThread(QThread):
    """
    """
    app = QtWidgets.QApplication(sys.argv)
    mainWindow =  MainWindow()
    def run(self):
        mainWindow.show()
        return self.app.exec_()
