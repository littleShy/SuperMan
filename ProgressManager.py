
# coding=utf-8
from eprogress import LineProgress,  MultiProgressManager

class ProgressManager:
    __MultiProgress__ = MultiProgressManager()
    __progressWidth__ = 40
    __progressSymbol__ = '■'
    childProgress = {}
    def __init__(self):
        pass
    
    def addLineProgress(self, progressID, progressName):
        progress = LineProgress(symbol=self.__progressSymbol__, width=self.__progressWidth__, title=progressName)
        self.childProgress[progressID] = progress
        self.__MultiProgress__.put(progressID, progress)
    
    def update(self, progressID, progress):
        self.__MultiProgress__.update(progressID, progress)

    def renameProgress(self, progressID, progressName):
        self.childProgress[progressID].title = progressName

progressManager = ProgressManager()
