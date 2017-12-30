import json
import random
import threading
from enum import Enum
from time import sleep

import ConstData
import FileOper
import logger
import NetTrans
# import ProgressManager

class TaskType(Enum):
    play = 2
    share = 3

class TaskType2(Enum):
    play = 1
    share = 3

class TaskType3(Enum):
    play = 3
    share = 2

class DoTaskType(Enum):
    doPlayTask = "play"
    doShareTask = "share"
    doQueryStatus = "query"
    doAllTask = "all"

class TaskStatus(Enum):
    allAvaliable = 0
    shareAvaliable = 1
    playAvaliable = 2
    accomplished = 3
    notEnough = 999

class Task:
    userName = ''
    taskDict = {}
    # lastTaskList = {
    #     'lastTaskName' : 'value',
    #     'unfinishedTask': ['taskname1', 'taskname2']
    # }
    tasksStatus = {
        'lastTaskName' : '',
        'unfinishedTask': []
    }
    currentTaskIndex = 0
    currentTaskName = '读取任务'
    errorCount = 0
    maxError = 1
    maxPlayIntervel = 320
    minPlayIntervel = 300
    maxTaskIntervel = 3
    minTaskIntervel = 1

    logger = logger.log
    netTrans = NetTrans.NetTrans()
    jsonDecoder = json.JSONDecoder()
    # progressManager = ProgressManager.progressManager
    totalProgressID = ''
    taskProgressID = ''
    usePlayInterval = True
    showProgress = False
    userVerification = False
    taskStatus = TaskStatus.allAvaliable.value
    doTaskType = DoTaskType.doAllTask.value

    def __init__(self, userName, authUrl, doTaskType=DoTaskType.doAllTask.value, maxError=1, usePlayInterval=True, showProgress=False, progressName='Task'):
        self.maxError = maxError
        self.doTaskType = doTaskType
        self.showProgress = showProgress
        self.usePlayInterval = usePlayInterval
        self.totalProgressID = progressName
        self.taskProgressID = self.totalProgressID + '-'
        if self.showProgress:
            self.addProgressBar()
        self.userName = userName
        if self.userAuth(authUrl) :
            self.userVerification = True
            if self.refreshTask() and self.showProgress:
                self.updateProgressBar(100)

    def userAuth(self, authUrl):
        jsonResult = self.netTrans.request(authUrl)
        if jsonResult == None:
            return False
        resuleDict = self.jsonDecoder.decode(jsonResult)
        result, msg = self.checkResult(resuleDict)
        if  result :
            self.netTrans.request(resuleDict['count_url'])
            self.viewCommonUrls()
            self.logger._log.debug('用户校验成功')
            return True
        else:
            self.logger._log.error('用户校验失败: %', msg)
            return False

    def viewCommonUrls(self):
        for urlDict in ConstData.commonUrls:
            for transType, url in urlDict.items():
                self.netTrans.request(url, NetTrans.TransType[transType])

    def checkResult(self, resuleDict):
        resuleCode = 0
        message = ''
        if 'code' in resuleDict.keys():
            resuleCode = resuleDict['code']
            if 200 == resuleDict['code'] or '200' == resuleDict['code']:
                return True, ''
            elif 'message' in resuleDict.keys():
                message = resuleDict['message']
            
        if 'succ' in resuleDict.keys():
            if 1 == resuleDict['succ'] or '1' == resuleDict['succ']:
                return True, ''
            elif 'message' in resuleDict.keys():
                message = resuleDict['message']
            
        self.logger._log.debug('success: %s, %s', str(resuleDict['succ']), message)

        if resuleCode != 500 :
            self.errorCount += 1        
        return False, message

    # taskList = {
    #     'taskname' : {
    #         'taskmoney': 'value',
    #         'taskuserappdo': 'value',
    #         'taskname': 'value',
    #         'taskid': 'value',
    #         'downloadtimes': 'value'
    #     },
    # }
    def initTaskListByOriTask(self, oriTaskList=[]):
        for oriTask in oriTaskList:
            task = {}
            task['taskmoney'] = oriTask['taskmoney']
            task['taskuserappdo'] = oriTask['taskuserappdo']
            task['taskname'] = oriTask['taskname']
            task['taskid'] = oriTask['taskid']
            task['downloadtimes'] = oriTask['downloadtimes']
            self.taskDict[task['taskname']] = task

    # lastTaskList = {
    #     'lastTaskName' : 'value',
    #     'unfinishedTask': ['taskname1', 'taskname2']
    # }
    def reInitTaskListWithLastTask(self, lastTaskList={}):
        self.logger._log.debug('上次任务完成情况: {}'.format(lastTaskList))
        if len(lastTaskList) != 0:
            if 'lastTaskName' in lastTaskList:
                self.currentTaskName = lastTaskList['lastTaskName']
                unfinishedTaskNameList = []
                if 'unfinishedTask' in lastTaskList:
                    unfinishedTaskNameList = lastTaskList['unfinishedTask']
                newDict = self.taskDict.copy()
                for taskName in self.taskDict:
                    if taskName == lastTaskList['lastTaskName']:
                        if taskName not in unfinishedTaskNameList:
                            del newDict[taskName]
                        break
                    if taskName not in unfinishedTaskNameList:
                        del newDict[taskName]
                self.taskDict = newDict

    def dumpTaskStatusList(self):
        userTaskStatus = {}
        userTaskStatus[self.userName] = self.tasksStatus
        FileOper.fileOper.writeObj(userTaskStatus)

    #任务的完成情况
    def recordUnfinishedTask(self, taskName):
        unfishedTasks = []
        if 'unfinishedTask' in self.tasksStatus:
            unfishedTasks = self.tasksStatus['unfinishedTask']
        else:
            self.tasksStatus['unfinishedTask'] = unfishedTasks
        if taskName not in unfishedTasks:
            unfishedTasks.append(taskName)
    
    def recordLastTask(self,taskName):
        self.tasksStatus['lastTaskName'] = taskName

    def refreshTask(self):
        jsonResult = self.netTrans.request(ConstData.taskUrls['tasks'], NetTrans.TransType['POST'])
        if jsonResult == None:
            self.errorCount += 1
            return False
        resuleDict = self.jsonDecoder.decode(jsonResult)
        result, msg = self.checkResult(resuleDict)
        if result :
            self.initTaskListByOriTask(resuleDict['data'])
            return True
        else:
            self.logger._log.error('获取任务失败: %', msg)
            return False

    #查询单个任务完成情况
    def taskStatus(self,taskName):
        currentTask = self.taskDict[self.currentTaskName]
        if currentTask['downloadtimes'] == "0" :
            return TaskStatus.notEnough.value
        dataDict = {'taskname':taskName, 'username': self.userName}
        jsonResult = self.netTrans.request(ConstData.taskUrls['taskStatus'], NetTrans.TransType['POST'], dataDict)
        if jsonResult == None:
            self.logger._log.warn('%s 任务状态获取失败!', self.currentTaskName)
            self.errorCount += 1
            return -1

        resuleDict = self.jsonDecoder.decode(jsonResult)
        result, msg = self.checkResult(resuleDict)
        if result :
            resultCode = resuleDict['jianshi']
            if resultCode == TaskStatus.accomplished.value:
                self.logger._log.debug('%s 任务状态 已完成',self.currentTaskName)
            elif resultCode == TaskStatus.shareAvaliable.value:
                self.logger._log.debug('%s 可做分享.', self.currentTaskName)
            elif resultCode == TaskStatus.playAvaliable.value:
                self.logger._log.debug('%s 任务状态 可试玩', self.currentTaskName)
            return resultCode
        else:
            if msg.find('此限量任务已被做完'):
                self.logger._log.warn('%s 任务状态 可用份数不足!',self.currentTaskName)
                return TaskStatus.notEnough.value
            self.logger._log.warn('%s 任务状态获取失败!', self.currentTaskName)
            return -1
    
    # 试玩任务完成
    # POST http://60.205.216.178:8080/uploads/fenxiang
    # money=0.8&username=ZZR152011&yuliu2=3&taskname=新郎微博2&taskid=312
    # 分享任务完成
    # money=0.3&username=ZZR153514&yuliu2=2&taskname=新郎微博2&taskid=330

    def getTaskDataDict(self,taskName,taskType, taskClass=1):
        currentTask = {}
        currentTask = self.taskDict[taskName]
        dataDict = {}
        if taskType == TaskType.play.value:
            dataDict['money'] = currentTask['taskmoney']
        elif taskType == TaskType.share.value:
            dataDict['money'] = currentTask['taskuserappdo']
        dataDict['username'] = self.userName
        realTaskType = taskType

        if taskClass == 2:
            if taskType == TaskType.play.value:
                realTaskType = TaskType2.play.value
            else:
                realTaskType = TaskType2.share.value
        elif taskClass == 3:
            if taskType == TaskType.play.value:
                realTaskType = TaskType3.play.value
            else:
                realTaskType = TaskType3.share.value

        dataDict['yuliu2'] = realTaskType
        dataDict['taskname'] = taskName
        dataDict['taskid'] = currentTask['taskid']
        return dataDict

    def addProgressBar(self):
        # self.progressManager.addLineProgress(self.totalProgressID,'{0: ^20}'.format(self.totalProgressID))
        # self.progressManager.addLineProgress(self.taskProgressID,'{0: >15}'.format(self.currentTaskName))
        pass

    def updateProgressBar(self, progress):
        if len(self.taskDict) == 0:
            totalProgress = 100
        else:
            totalProgress = self.currentTaskIndex/len(self.taskDict) * 100
        # self.progressManager.update(self.totalProgressID, totalProgress)
        # self.progressManager.renameProgress(self.taskProgressID, '{0: >15}'.format(self.currentTaskName))
        # self.progressManager.update(self.taskProgressID, progress)

    #试玩任务
    def _doTask(self, taskName, taskType):
        for i in range(1, 4):
            if i != 1:
                self.logger._log.debug('%s 第%d次尝试!', taskName, i)
            dataDict = self.getTaskDataDict(taskName, taskType, i)
            jsonResult = self.netTrans.request(ConstData.taskUrls['doTask'],dataDict=dataDict)
            if jsonResult == None:
                self.errorCount += 1
                return false
            resuleDict = self.jsonDecoder.decode(jsonResult)
            result, msg = self.checkResult(resuleDict)
            if result:
                return True
            elif -1 == msg.find('网络延时'):
                return False
        return False
    
    def doTask(self, lastTasks={}):
        if not self.userVerification:
            return
        self.logger._log.debug('=======开始做任务=======')
        self.currentTaskIndex = 0
        self.reInitTaskListWithLastTask(lastTasks)

        for task in self.taskDict.values() :

            self.currentTaskName = task['taskname']
            taskStatus = self.taskStatus(self.currentTaskName)

            if taskStatus != TaskStatus.accomplished.value and self.doTaskType != DoTaskType.doQueryStatus.value :
                if taskStatus == TaskStatus.notEnough.value:
                    self.recordUnfinishedTask(self.currentTaskName)
                else:
                    if (taskStatus == TaskStatus.allAvaliable.value or taskStatus == TaskStatus.playAvaliable.value) \
                    and (self.doTaskType == DoTaskType.doPlayTask.value or self.doTaskType == DoTaskType.doAllTask.value):
                        self.logger._log.debug('%s 试玩中...', self.currentTaskName)
                        if self.usePlayInterval:
                            self.randomSleep(self.minPlayIntervel, self.maxPlayIntervel)
                        if self._doTask(self.currentTaskName, TaskType.play.value) :
                            self.logger._log.debug('%s 试玩完成.', self.currentTaskName)
                        else:
                            self.recordUnfinishedTask(self.currentTaskName)
                            self.logger._log.error('%s 试玩失败!', self.currentTaskName)
                    
                    if (taskStatus == TaskStatus.allAvaliable.value or taskStatus == TaskStatus.shareAvaliable.value) \
                    and (self.doTaskType == DoTaskType.doAllTask.value or self.doTaskType == DoTaskType.doShareTask.value):
                        self.logger._log.debug('%s 分享中...', self.currentTaskName)
                        if self._doTask(self.currentTaskName, TaskType.share.value) :
                            self.logger._log.debug('%s 分享完成.', self.currentTaskName)
                        else:
                            self.recordUnfinishedTask(self.currentTaskName)
                            self.logger._log.error('%s 分享失败!', self.currentTaskName)
            self.currentTaskIndex += 1
            self.randomSleep(self.minTaskIntervel, self.maxTaskIntervel)
            if int(self.errorCount) >= int(self.maxError) and int(self.maxError) != -1:
                self.logger._log.warn('失败次数已达上限!')
                break
        self.recordLastTask(self.currentTaskName)
        self.dumpTaskStatusList()
        self.logger._log.debug('=======任务已完成=======')
    def randomSleep(self, start, stop):
        randomSecond = random.randrange(start ,stop)
        totalProgress = randomSecond * 2
        for i in range(1, totalProgress+1):
            if self.showProgress:
                self.updateProgressBar(i/totalProgress * 100)
            sleep(0.5)
