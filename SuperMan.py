import sys
from enum import Enum

from PyQt5.QtCore import QThread

import logger
sys.path.append('UI')
import MainWindow
import TaskThread



class MainClass(object):
    """
    """
    threads = []
    app = None
    uiThread = MainWindow.UIThread()
    taskThread = TaskThread.TaskThread()
    def __init__(self):
        self.signalSlot()
  
    def signalSlot(self):
        self.uiThread.mainWindow.netClassifyChangedSignal.connect(self.taskThread.setNetClassify)
        self.uiThread.mainWindow.usePlayInterValSignal.connect(self.taskThread.setUsePlayInterval)
        self.uiThread.mainWindow.doTaskTypeChangedSignal.connect(self.taskThread.setDoTaskType)
        self.uiThread.mainWindow.beginDoTaskSignal.connect(self.taskThread.start())
        self.taskThread.allTaskFinishedSignal.connect(self.uiThread.mainWindow.on_doTask_clicked)

    def start(self):
        self.uiThread.start()

# getOption()
# TaskThread.TaskThread().start(doTaskType, netClassify, maxError, usePlayInterval, showProgress)
MainClass().start()
input('所有任务已结束,回车退出!')
