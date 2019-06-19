# encondding = utf - 8
#用于实现具体动作，比如输入数据框
from selenium import webdriver
from config.VarConfig import ieDriverFilePath
from config.VarConfig import chromeDriverFilePath
from config.VarConfig import firefoxDriverFilePath
from util.ObjiectMap import getElement,getElements
from selenium.webdriver.support.ui import Select
from util.ClipboardUtil import Clipbard
from util.KeyBoradUtil import KeyboardKeys
from util.DirAndTime import *
from util.WaitUtil import WaitUtil
# from config.VarConfig import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium.webdriver.common.keys import Keys
import json
# 定义全局变量
driver = None

# 全局的等待类实例对象
waitUtil = None


def open_browser(browserName, *args):
    # 打开浏览器
    global driver,waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path=ieDriverFilePath)
        elif browserName.lower() == 'Firfox':
            driver = webdriver.Firefox(executable_path=firefoxDriverFilePath)
            # driver = webdriver.Chrome(executable_path=chromeDriverFilePath)
            # # 创建chrome浏览器的一个options实例对象
            # chrome_options = Options()
            # # 添加屏蔽 ---ignore -certificate --errors
            # chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            # driver = webdriver.Chrome(executable_path=chromeDriverFilePath,
            #                           chrome_options=chrome_options)

        else:

            driver = webdriver.Chrome(executable_path=chromeDriverFilePath)


        # driver 对象创建成果，创建等待类实例对象
        waitUtil = WaitUtil(driver)

    except Exception as e:
        raise e


# 使用cooki登录新的页面
def new_browser(url):
    # driver = webdriver.Chrome()
    driver.delete_all_cookies() #清除所有cookie
    driver.set_page_load_timeout(20)
    driver.set_script_timeout(20)
    try:
        driver.get(url)
    except:
        driver.execute_script("window.stop()")
    time.sleep(5)
    f1 = open(r'D:\coed\automation\web_ShiYue\KeyWordFromeWork-master\testData\cookies6.11.01.txt')
    cookies = f1.read()
    cookies = json.loads(cookies)
    #添加cookie到未登的录页面
    for co in cookies:
        driver.add_cookie(co)
    driver.refresh() #再次刷新页面则得到登陆后的界面
    time.sleep(5)
    # driver.close()

def visit_url(url,*arg):
    # 访问某个网站
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e


def close_browser(*arg):
    # 关闭浏览器
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e


def sleep(sleepSeconds, *arg):
    # 强制等待
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e


def clear(loctaionType, locatiorExpression, *arg):
    # 清除输入框默认内容
    global driver
    try:
        getElement(driver, loctaionType, locatiorExpression).clear()
    except Exception as e:
        raise e


def input_string(locationType, locatorExpression, inputContent):
    # 在页面输入框中输入数据
    global driver
    try:
        getElement(driver, locationType, locatorExpression).send_keys(inputContent)
        # print(inputContent)
    except Exception as e:
        raise e


def click(locationType, locatorExpression, *arg):
    # 单击页面元素
    global driver
    try:
        getElement(driver, locationType, locatorExpression).click()
    except Exception as e:
        raise e


def assert_string_in_pagesource(assertSring, *arg):
    # 断言页面源码是否存在某关系字或者关键字符串中
    global driver,waitUtil
    try:
        assert assertSring in driver.page_source, ("%s not foud in page source!" )% assertSring
    except ArithmeticError as e:
        raise  ArithmeticError(e)
    except Exception as  e:
        raise e



def assert_title(titleStr, *args):
    # 断言页面标题是否存在给定的关键字符串
    global driver,waitUtil
    try:
        assert titleStr in driver.title, \
            "%s not found in title!" % titleStr
    except ArithmeticError as e:
        raise ArithmeticError(e)
    except Exception as  e:
        raise e


def getTitle(*arg):
    # 获取页面标题
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e
def getPageSouce(*arg):
    global driver
    try:
        return driver.page_source
    except Exception as e:
        raise e


def switch_to_frame(locationType, frameLocatorExpression, *arg):
    # 切换进入frame
    global driver
    try:
        driver.switch_to.frame(getElement
                               (driver, locationType, frameLocatorExpression))
    except Exception as e:
        print("frame error")
        raise e


def switch_to_default_content(*arg):
    # 切出frame
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e
#点击多选框


def clickCheckBox(locationType,framelocatorExpression,*args):
    global driver,waitUtil
    try:
        ListElement=getElements(driver,locationType,framelocatorExpression)
        print(ListElement)
        for element in ListElement:
            element.click()

    except Exception as e:
        raise e

# #下拉列表选择
# def selecter_list(locationType,framelocatorExpression,textValue,*args):
#     global driver,waitUtil
#     try:
#         select_element=Select(getElement(driver,locationType,framelocatorExpression))
#         select_element.select_by_visible_text(textValue)
#         value= select_element.all_selected_options[0].text
#         assert value==textValue,"断言失败,当前选择的不是%s"%textValue
#     except AssertionError as e:
#         raise AssertionError(e)
#     except Exception as e:
#         raise e
#     else:
#         logger.info("\033[1;32;m关键字%s选择成功\033[0m" % textValue)




def paste_string(pasteString, *arg):
    # 模拟操作Ctrl+ v 操作
    global driver
    try:
        Clipbard.setTest(pasteString)
        # 等待2秒，防止代码执行的太快，而未成功粘贴内容
        time.sleep(2)
        KeyboardKeys.twoKeys("ctrl", "v")
    except Exception as  e:
        raise e


def press_tab_key(*arg):
    # 模拟tab键
    try:
        KeyboardKeys.oneKey("tab")
    except Exception as e:
        raise e


def press_enter_key(*arg):
    # 模拟enter键
    try:
        KeyboardKeys.oneKey("enter")
    except Exception as e:
        raise e


def maximize_brower():
    # 窗口最大化
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e


def capture_screen(*args):
    # 截取屏幕图片
    global driver
    currTime = getCurrentTime()
    picNameAndPath = str(createCureenDateDir()) + "\\" + str(currTime) + ".Png"
    try:
        driver.get_screenshot_as_file(picNameAndPath.replace('\\', r'\\'))
    except Exception as e:
        raise e
    else:
        return picNameAndPath

def waitPressenceOfElementLocated(locationType, locatorExprexxion, *arg):
    # 显示等待页面元素出现的DOM中，但并不一定可见 存在则返回页面元素对象
    global waitUtil
    try:
        waitUtil.presenceOfeElmentLocated(locationType, locatorExprexxion)
    except Exception as e:
        raise e


def waitFrameToBeAvailableAndSwitchToIt(locationType, locatorExprexxion, *args):
    # 检查frame 是否存在，存在则切换进frame控件中
    global  driver
    try:
        driver.switch_to.frame(getElement(driver,locationType, locatorExprexxion))
    except Exception as e:
        # print("error...")
        raise e


def waitVisibilityOfElementLocated(locationType, locatorExprexxion):
    # 显示等待页面元素出现在DOM 中并且可见，存在返回该页面元素对象
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType, locatorExprexxion)
    except Exception as e:
        raise e


if __name__ =="__main__":
    assert_string_in_pagesource("发送成功")