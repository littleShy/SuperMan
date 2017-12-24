import threading
import Task
import ConstData
import logger
import FileOper
import os
from PyQt5.QtCore import QThread, pyqtSignal

class TaskThread(QThread):
    netClassifyList = ['unicom', 'chinanetA', 'chinanetB', 'chinanetC']
    logger = logger.log
    threadList = []
    missionList = []
    tasksStatus = []
    userNameList = []
    fileOper = FileOper.fileOper

    allTaskFinishedSignal = pyqtSignal(bool)

    netClassify = ''
    doTaskType = 'all'
    maxError = 1
    usePlayInterval = True
    showProgress = False
    getAds = True
    def setNetClassify(self, index):
        if 0 == index:
            self.netClassify = 'unicom'
        elif 1 == index:
            self.netClassify = 'chinanetA'
        elif 2 == index:
            self.netClassify = 'chinanetC'
        elif 3 == index:
            self.netClassify = 'chinanetC'

    def setDoTaskType(self, index):
        doTaskType = index
    
    def setMaxError(self, maxError):
        self.maxError = maxError
    
    def setUsePlayInterval(self, usePlayInterval):
        self.usePlayInterval = usePlayInterval

    def setShowProgress(self, showProgress):
        self.showProgress = showProgress
    
    def setGetAds(self, getAds):
        self.getAds = getAds

    def run(self):
        print('doTaskType:{}, maxError:{}, usePlayInterval:{}, showProgress:{}, getAds:{}.'.format(\
        self.doTaskType, self.maxError,self.usePlayInterval,self.showProgress, self.getAds))
        return
        lastTaskStatusList = self.getLastTasksStatus()
        userAuth = []
        if self.netClassify in ConstData.userAuthList:
            userAuth = ConstData.userAuthList[self.netClassify]
        else:
            self.logger._log.error('网络类型参数错误: %s, 可用的网络类型: %s',self.netClassify, ConstData.userAuthList.keys())
            return
        self.logger._log.debug('用户总数: %s', len(userAuth.keys()))
        for userName in userAuth.keys():
            lastTaskStatus = {}
            if userName in lastTaskStatusList:
                lastTaskStatus = lastTaskStatusList[userName]
            if userName in ConstData.comment.keys():
                userComment = ConstData.comment[userName]
                comment = ''
                for value in userComment.values():
                    comment += value + '-'
            threadName = comment + userName
            task = Task.Task(userName, userAuth[userName], self.maxError, self.usePlayInterval, self.showProgress, threadName)
            thd = threading.Thread(target=task.doTask,args=(lastTaskStatus, self.doTaskType,),name=threadName)
            thd.setDaemon(False)
            thd.start()
            self.userNameList.append(userName)
            self.missionList.append(task)
            self.threadList.append(thd)
        for thd in self.threadList :
            thd.join()

        self.allTaskFinishedSignal.emit(False)
    
    def getLastTasksStatus(self):
        lastTasksStatus = {}
        while not self.fileOper.reachEnd():
            lastTask = self.fileOper.readObj()
            if lastTask == None:
                break
            lastTasksStatus.update(lastTask)
        if self.doTaskType == Task.DoTaskType.doAllTask:
            self.fileOper.clean()
        return lastTasksStatus
