#encoding = utf - 8
#用于实现将数据设置到剪切板中
import win32clipboard as w
import  win32con

class Clipbard(object):
    #模拟windows设置剪切板
    #读取剪切板
    @staticmethod
    def getText():
        #打开剪切板
        w.OpenClipboard()

        #获取剪切板中的数据
        d = w.GetClipboardData(win32con.CF_TEXT)

        #关闭剪切板
        w.CloseClipboard()

        #返回剪切板数据给调用者
        return d

    #设置剪切板中的内容
    @staticmethod
    def setTest(aString):
        #打开剪切板
        w.OpenClipboard()

        #清空剪切板
        w.EmptyClipboard()

        #讲数据aString写入剪切板
        w.SetClipboardData(win32con.CF_UNICODETEXT,aString)

        #关闭剪切板
        w.CloseClipboard()
