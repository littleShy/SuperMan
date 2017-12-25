import threading
import Task
import ConstData
import logger
import FileOper
import os

class TaskThread:
    logger = logger.log
    threadList = []
    missionList = []
    tasksStatus = []
    userNameList = []
    fileOper = FileOper.fileOper

    netClassify = ''
    doTaskType = Task.DoTaskType.doAllTask.value
    maxError = 1
    usePlayInterval = True
    showProgress = False
    getAds = True

    def __init__(self, doTaskType=Task.DoTaskType.doAllTask.value, netClassify='', maxError=1, usePlayInterval=True, showProgress=False, getAds=True):
        self.doTaskType = doTaskType
        self.netClassify = netClassify
        self.maxError = maxError
        self.usePlayInterval = usePlayInterval
        self.showProgress = showProgress
        self.getAds = getAds
    
    def start(self):
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
            task = Task.Task(userName, userAuth[userName], self.doTaskType, self.maxError, self.usePlayInterval, self.showProgress, threadName)
            thd = threading.Thread(target=task.doTask,args=(lastTaskStatus,),name=threadName)
            thd.setDaemon(False)
            thd.start()
            self.userNameList.append(userName)
            self.missionList.append(task)
            self.threadList.append(thd)
        for thd in self.threadList :
            thd.join()
    
    def getLastTasksStatus(self):
        lastTasksStatus = {}
        while not self.fileOper.reachEnd():
            lastTask = self.fileOper.readObj()
            if lastTask == None:
                break
            lastTasksStatus.update(lastTask)
        if self.doTaskType == Task.DoTaskType.doAllTask.value:
            self.fileOper.clean()
            print('delete all')
        else:
            print('dont delete: ', self.doTaskType, )
        return lastTasksStatus
