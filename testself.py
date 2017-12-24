import NetTrans
import Task
import ConstData
import sys
import os
import FileOper
import pickle
import logger
from time import sleep
import ProgressManager
import json

def runTaskTest():
    # play = 2
    # share = 3
    # queryStatus = 10

    username = 'ZZR212016'
    taskname = '9秀.'
    taskid = '336'
    taskmoney = 1.4
    yuliu2 = 1

    # task = Task.Task(username)

    dataDict = {}

    dataDict['money'] = taskmoney
    dataDict['username'] = username
    dataDict['yuliu2'] = yuliu2
    dataDict['taskname'] = taskname
    dataDict['taskid'] = taskid

    statusDict = {'taskname':taskname, 'username': username}

    jsonResult = NetTrans.NetTrans().request(ConstData.taskUrls['tasks'],NetTrans.TransType['POST'], {})
    # jsonResult = NetTrans.NetTrans().request(ConstData.taskUrls['taskStatus'],NetTrans.TransType['POST'], statusDict)
    # jsonResult = NetTrans.NetTrans().request(ConstData.taskUrls['doTask'],NetTrans.TransType['POST'], dataDict)

    print (jsonResult)
    # 试玩
    # POST http://60.205.216.178:8080/uploads/fenxiang
    # money=0.8&username=ZZR152011&yuliu2=3&taskname=新郎微博2&taskid=312
    # 分享任务完成
    # money=0.3&username=ZZR153514&yuliu2=2&taskname=新郎微博2&taskid=330

def fileOperTest():
    data = {1:['中文','中文2','中文3'],2:{'也是中文':1}}
    FileOper.fileOper.writeObj(data)
    while not FileOper.fileOper.reachEnd():
        dataRead = FileOper.fileOper.readObj()
        print ('dataRead type: {}, data: \n{}'.format(type(dataRead), dataRead))
#    FileOper.fileOper.clean()
	
def fileTest():
    filename = 'RunTimeData/RunTimeConfig.dat'
    file = open(filename, 'w+')
    data = {'1':1,'2':2,'3':3}
    # pickle.dump(data, file)
    # data1 = {'3':1,'2':2,'1':3}
    # pickle.dump(data1, file)
    # file.close()

    # file = open(filename, 'rb+')
    # while file.tell() < size:
    #     dataRead = pickle.load(file)
    #     print(dataRead)

    file.write(str(data)+'\n')
    file.close()
    size = os.path.getsize(filename)
    file = open(filename, 'r+')
    file.readline()
    print('getsize: {}, tell: {}'.format(size, file.tell()))
    file.close()

def testLog():
    logger.log._log.debug('测试日志!')

def testProgress():
    ProgressManager.progressManager.addLineProgress('1', 'name 1')
    ProgressManager.progressManager.addLineProgress('2', 'name 2')

    for i in range(1, 101):
        ProgressManager.progressManager.update('1', i)
        sleep(0.5)

def testJson():
	data = {'中文1':123,  '中文2':234}
	decoder = json.JSONDecoder()
	encoder = json.JSONEncoder(ensure_ascii=False)
	encoderStr = encoder.encode(data)
	print('encoderStr:',  encoderStr)
	
	decoderObj = decoder.decode(encoderStr)
	print('type: {}, decoderObj: {}'.format(type(decoderObj),  decoderObj))

#fileOperTest()
runTaskTest()
# fileTest()
# testLog()
# testProgress()
#testJson()

# import ProgressManager
# import time

# ProgressManager.progressManager.addLineProgress('1', '任务1')
# # ProgressManager.progressManager.addLineProgress('2', '    任务2')
# # ProgressManager.progressManager.addLineProgress('3', '任务3')


# for i in range(1, 101):
#     # if i == 25:
#     #     ProgressManager.progressManager.addLineProgress('4', '    任务4')
#     if i % 3 == 0:
#         ProgressManager.progressManager.update('1', i )
#         ProgressManager.progressManager.renameProgress('1', '修改'+str(i))
#     # if i % 5 == 0:
#     #     ProgressManager.progressManager.update('2', i )
#     #     ProgressManager.progressManager.renameProgress('2', '修改'+str(i))
#     # if i % 6 == 0 :
#     #     ProgressManager.progressManager.update('3', i )
#     #     ProgressManager.progressManager.renameProgress('3', '修改'+str(i))
#     # if i % 7 == 0 and i >= 25:
#     #     ProgressManager.progressManager.update('4', i)
#     #     ProgressManager.progressManager.renameProgress('4', '修改'+str(i))
#     time.sleep(0.2)



# from ctypes import windll, create_string_buffer

# # stdin handle is -10
# # stdout handle is -11
# # stderr handle is -12

# h = windll.kernel32.GetStdHandle(-12)
# csbi = create_string_buffer(22)
# res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)

# if res:
#     import struct
#     (bufx, bufy, curx, cury, wattr,
#      left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
#     sizex = right - left + 1
#     sizey = bottom - top + 1
# else:
#     sizex, sizey = 80, 25 # can't determine actual size - return default values

# print (sizex, sizey)


# import curses

# stdscr = curses.initscr()
# curses.resizeterm(150, 200)

# curses.endwin()


# from term import opentty, cbreakmode

# with opentty() as tty:
#     if tty is not None:
#         with cbreakmode(tty, min=0):
#             tty.write('\033[8;25;80t');

# print ('terminal resized')
