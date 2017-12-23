import logging
import logging.handlers
import time
import os

class Logger:
    __logFile__ = 'RunTimeLog ' + time.strftime('%Y-%m-%d',time.localtime()) + '.log'
    __logName__ = 'SuperMan'
    dirName = 'RunTimeData'
    fileFullName = dirName + '/' + __logFile__
    _log = None
    
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        
    __handler__ =  logging.handlers.RotatingFileHandler(fileFullName, maxBytes = 1024*1024, backupCount = 5) # 实例化
    __fmt__ = '%(asctime)s - %(filename)s:%(lineno)s[%(threadName)s] %(message)s'
    __formatter__ = None
    def __init__(self):
        self.__formatter__ = logging.Formatter(self.__fmt__)   # 实例化formatter
        self.__handler__.setFormatter(self.__formatter__)      # 为handler添加formatter

        self._log = logging.getLogger(self.__logName__)    # 获取名为tst的logger
        self._log.addHandler(self.__handler__)           # 为logger添加handler
        self.setLevel(logging.DEBUG)

    def setLevel(self, logLevel):
        self._log.setLevel(logLevel)

    def log(self, level, message, *args, **kwargs):
        self._log.log(level, message, args, **kwargs)

    def debug(self, message):
        # message = '~_~ ' + message
        self._log.debug(message)

    def error(self, message, *args, **kwargs):
        # message = '˙０˙ ' + message
        self._log.error(message, args, **kwargs)

    def warn(self, message, *args, **kwargs):
        # message = 'o_O ' + message
        self._log.warn(message, args, **kwargs)

log = Logger()