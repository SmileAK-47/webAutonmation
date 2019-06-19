#enconding = utf- 8
#用于实现定位页面元素
from selenium.webdriver.support.ui import WebDriverWait

#获取单个页面元素对象
def getElement(driver, locationType,locatorExpression):
    try:
        element = WebDriverWait(driver,30,0.3).until\
            (lambda x:x.find_element(by = locationType,value = locatorExpression))
        return element
    except Exception as e:
        print("查询元素超时", e)

#获取多个相同的页面元素对象,一list返回
def getElements(driver, locationType, locatiorExpression):
    try:
        elements = WebDriverWait(driver,30 ,0.3).until\
            (lambda x:x.find_elements(by = locationType , value = locatiorExpression))
        return  elements
    except Exception as e :
        print("查询元素超时", e)

if __name__ == '__main__':
    from selenium import webdriver

    #进行单元测试
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    searchaBox = getElement(driver,"id","kw")

    #打印页面对象的标签名
    print(searchaBox.tag_name)
    aList = getElements(driver,"tag name","a")
    print(len(aList))
    driver.quit()