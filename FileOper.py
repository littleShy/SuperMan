import pickle
import threading
import os
import logger
import sys
import json

class FileOper:
    _lock = None
    fileName = 'RunTimeConfig.dat'
    dirName = 'RunTimeData'
    log = logger.log
    filePos = 0
    jsonDecoder = json.JSONDecoder()
    jsonEncoder = json.JSONEncoder(ensure_ascii=False)
    @property
    def lock(self):
        return self._lock

    def __init__(self, fileName='RunTimeConfig.dat', forWrite=True):
        if not os.path.exists(self.dirName):
            os.makedirs(self.dirName)
        self._lock = threading.Lock()
        self.fileName = self.dirName + '/' + fileName
        self.forWrite = forWrite

    def writeObj(self, obj):
        with self.lock:
            try:
                with open(self.fileName, 'a+') as fh:
                    # pickle.dump(obj, fh)
                    objStr = self.jsonEncoder.encode(obj)
                    fh.write(objStr + '\n')
            except:
                self.log._log.error('写文件失败!%s', sys.exc_info()[1])

    def readObj(self):
        with self.lock:
            try:
                if not os.path.exists(self.fileName):
                    return None
                if self.filePos == os.path.getsize(self.fileName):
                    return None
                with open(self.fileName, 'r+') as fh:
                    fh.seek(self.filePos)
                    # obj = pickle.load(fh)
                    obj = self.jsonDecoder.decode(fh.readline())
                    self.filePos = fh.tell()
                return obj
            except:
                print(sys.exc_info()[1])
                self.log._log.error('读文件失败!%s', sys.exc_info()[1])
            return None
    
    def clean(self):
        with self.lock:
            try:
                if not os.path.exists(self.fileName):
                    return
                with open(self.fileName, 'wb+') as fh:
                    fh.truncate()
            except:
                self.log._log.error('清空文件失败!%s', sys.exc_info()[1])
    
    def reachEnd(self):
        with self.lock:
            try:
                if self.filePos == os.path.getsize(self.fileName):
                    return True
                else:
                    return False
            except:
                self.log._log.error('获取文件状态失败!%s', sys.exc_info()[1])
            return True

fileOper = FileOper()
