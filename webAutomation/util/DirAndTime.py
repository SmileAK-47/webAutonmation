#encoding =utf - 8
#获取当前日期及时间  以及创建异常截图存放目录
import os
from  datetime import datetime
from config.VarConfig import screenPicturesDir
import  time
#获取当前的日期
def getCurrentDate():
    timeTup = time.localtime()
    getCurrentDate = str(timeTup.tm_year) + "-" + \
        str(timeTup.tm_mon) + "-" + str(timeTup.tm_mday)
    return getCurrentDate

#获取当前的时间
def getCurrentTime():
    timeStr = datetime.now()
    nowTime = timeStr.strftime('%H-%M-%S-%f')
    return nowTime

#创建截图存放目录
def createCureenDateDir():
    dirName = os.path.join(screenPicturesDir,getCurrentDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    return dirName

if __name__ =='__main__':
    print(getCurrentDate())
    print(getCurrentTime())
    print(createCureenDateDir())
          