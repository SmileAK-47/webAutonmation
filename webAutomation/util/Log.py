#encoding = utf -8
import logging
import logging.config
from config.VarConfig import parentDirPath
from  logwrap import LogWrap
# 读取日志配置文件
# print(parentDirPaht)
logging.config.fileConfig(parentDirPath+"\config\Logger.conf")
# print(parentDirPaht+"\config\Logger.conf")
#选择一个日志格式
logger=logging.getLogger("example02") #或者example01

# logwrap =LogWrap
def debug(message):
    #定义dubug级别日志打印方法
    logger.debug(message)

def info(message):
    #定义info级别日志打印方法
    logger,info(message)

def warning(message):
    #定义warnging级别日志打印方法
    logger.warning(message)
