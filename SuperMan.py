import sys
from enum import Enum

import logger
import MainWindow
import TaskThread

sys.path.append('UI')

class ArgOption(Enum):
    net = '--net-type'
    showProgress = '--show-progress'
    doTaskType = '--do-task-type'
    maxError = '--max-error'
    usePlayInterval = '--use-play-interval'

netClassify = ''
showProgress = False
doTaskType = 'all'
usePlayInterval = True
maxError = 1

class MainClass(object):
    """
    """
    app = None
    mainWindow = QtWidgets.QMainWindow()
    taskThread = TaskThread.TaskThread()
    def __init__(self):
        ui = MainWindow(mainWindow)

    def handleUI(self):
        """
        """
        self.app = QtWidgets.QApplication(sys.argv)
        self.mainWindow.show()
        return self.app.exec_()
    
    def signalSlot(self):
        self.mainWindow.netClassifyChangedSignal.connect(self.taskThread.)

    def handleData(self):
        self.taskThread.start()



def _getOption(option, boolOption=False):
    if option in sys.argv :
        optionIndex = sys.argv.index(option) + 1
        if optionIndex < len(sys.argv):
            optValue = sys.argv[optionIndex]
            if boolOption:
                if str(optValue.lower()) == 'true':
                    return True
                elif str(optValue.lower()) == 'false':
                    return False
            else:
                return optValue
    return None

def getOption():
    global netClassify, showProgress, doTaskType, maxError, usePlayInterval
    optValue = _getOption(ArgOption.net.value)
    if optValue != None:
        netClassify = optValue
    optValue = _getOption(ArgOption.showProgress.value, True)
    if optValue != None:
        showProgress = optValue
    optValue = _getOption(ArgOption.doTaskType.value)
    if optValue != None:
        doTaskType = optValue
    optValue = _getOption(ArgOption.maxError.value)
    if optValue != None:
        maxError = optValue
    optValue = _getOption(ArgOption.usePlayInterval.value, True)
    if optValue != None:
        usePlayInterval = optValue

getOption()
TaskThread.TaskThread().start(doTaskType, netClassify, maxError, usePlayInterval, showProgress)

input('所有任务已结束,回车退出!')
