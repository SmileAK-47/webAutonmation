# encoding = utf-8
from selenium import webdriver
import unittest, time
import logging, traceback
import ddt
from test000.ExcelUtil01 import ParseExcel
from selenium.common.exceptions import NoSuchElementException

# 初始化日志对象
logging.basicConfig(

    # 日志级别
    level=logging.INFO,
    # 日志格式
    # 时间，代码所在的文件名，代码行号，日志级别名字，日志信息
    format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s',
    # 打印日志时间
    datefmt='%a,%y-%m-%d %h:%m:%s',
    # 打印日志文件存放目录（目录必须存在）及日志文件名
    filename=r'G:\KeyWordFromeWork\testData\logg.log',

    # 打开日志文件的方式
    filemode='w'
    #打印到控制台

)

excelPath = r"G:\KeyWordFromeWork\testData\NBA.xlsx"
sheetName = '搜索数据'
# 创建ParseExcel类的实力对象
excel = ParseExcel(excelPath, sheetName)


@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @ddt.data(*excel.getDateaFromSheet())
    def test_dataDrivenByFile(self, data):
        testData, expectData = tuple(data)
        url = "http://www.baidu.com"
        # 访问百度首页
        self.driver.get(url)
        # 将窗口最大化
        self.driver.maximize_window()
        print(testData, expectData)
        # 设置饮食等待时间为10秒
        self.driver.implicitly_wait(10)
        try:
            # 找到搜索输入框，并输入测试数据
            self.driver.find_element_by_id("kw").send_keys(testData)

            # 找到搜索按钮，并单击
            self.driver.find_element_by_id('su').click()
            time.sleep(3)
            # page_source = self.driver.page_source
            # print(page_source)
            # 断言期望结构是否出现在页面源码中

            self.assertTrue(expectData in  self.driver.page_source)

        except NoSuchElementException as e:
            logging.error('页面元素不存在' + str(traceback.format_exc()))
        except AssertionError as e:
            logging.info("'搜索'%s ,'期望'%s,'失败'" % (testData, expectData))
        except Exception as e:
            logging.error('未知错误，错误信:' + str(traceback.format_exc()))
        else:
            logging.info("'搜索'%s',期望'%s '通过'" % (testData, expectData))

    def testDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
