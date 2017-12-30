# encoding=utf-8
import sys
import gzip
import time
import urllib
import http.cookiejar
import urllib.request
from enum import Enum
import logger

class TransType(Enum):
    GET = 1
    POST = 2

class NetTrans:
    __url__ = ''
    __dataDict__ = {}
    __header__ = []

    __logger__ = logger.log
    __ckJar__ = http.cookiejar.CookieJar()
    __ckProcessor__ = urllib.request.HTTPCookieProcessor(__ckJar__)
    #带cookie
    __ckOpener__ = urllib.request.build_opener(__ckProcessor__)
    #不带cookie
    __opener__ = urllib.request.build_opener()
    
    def __initOpener__(self):
        self.__header__.append(['Accept-Encoding','gzip'])
        self.__header__.append(['User-Agent', 'okhttp/3.3.1'])
        self.__header__.append(['Connection', 'Keep-Alive'])
        self.__opener__.addheaders = self.__header__
    
    #带cookie
    def __initCkOpener__(self):
        self.__header__.append(['Accept-Encoding','gzip'])
        self.__header__.append(['User-Agent', 'okhttp/3.3.1'])
        self.__header__.append(['Connection', 'Keep-Alive'])
        self.__ckOpener__.addheaders = self.__header__
    
    def __initPostData__(self, dataDict):
        postData = urllib.parse.urlencode(dataDict).encode()
        return postData

#unzip response
    def __ungzip__(self, data):
        outData = ''
        try:
            outData = gzip.decompress(data)
        except:
            self.__logger__._log.error(sys.exc_info()[1])
            self.__logger__._log.warn('No need to decompress data!')
        return outData

    def __decodeResponseContent__(self, response):
        try:
            contentEncode = response.info().get('Content-Encoding')
        except KeyError:
            return response.read().decode()
        except:
            self.__logger__._log.error(sys.exc_info()[1])
            return None

        # self.__logger__._log.debug('Content-Encoding: %s', contentEncode)
        if contentEncode == 'gzip':
            return self.__ungzip__(response.read()).decode()
        else:
            return response.read().decode()

    def request(self, url, transType=TransType['POST'], dataDict={}):
        response = None
        try:
            self.__initOpener__()
            if transType is TransType.POST :
                postData = self.__initPostData__(dataDict)
                response = self.__opener__.open(url, postData)
            else:
                response = self.__opener__.open(url)
        except :
            self.__logger__._log.error('连接失败: %s', sys.exc_info()[1])
            if response != None:
                responseCode = response.getcode()
                self.__logger__._log.error('Response Code: %d', responseCode)
            return None

        return self.__decodeResponseContent__(response)

    def ckRequest(self, url, transType=TransType['POST'], dataDict={}):
        self.__initOpener__()
        if transType is TransType().POST :
            postData = self.__initPostData__(dataDict)
            response = self.__ckOpener__.open(url, postData)
        else:
            response = self.__ckOpener__.open(url)
        
        return self.__decodeResponseContent__(response)
