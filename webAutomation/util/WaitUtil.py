#enconding = utf-8
#智能等待页面元素出现
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtil(object):
    def __init__(self,driver):
        self.locationTypeDict = {
            "xpath":By.XPATH,
            "id":By.ID,
            "name":By.NAME,
            "class_naem":By.CLASS_NAME,
            "tag_name":By.TAG_NAME,
            "link_text":By.LINK_TEXT,
            "partial_link_test":By.PARTIAL_LINK_TEXT
        }
        self.driver = driver
        self.wait = WebDriverWait(self.driver,30)

    '''
      def frame_available_and_switch_to_it(self,locationType,locatoExpression):
          #检查frame是否存在，存在则切换金frame 控件中
          try:
              self.wait.until(EC.frame_to_be_available_and_switch_to_it((self.locationTypeDict[locationType.lower()],locatoExpression)))
          except Exception as e:
              raise e

      def visibility_element_located(self,loactionType,locatoExpression):
          #显式等待 页面元素出现
          try:
              element = self.wait.until(EC.visibility_of_element_located((self.locationTypeDict[loactionType.lower()],locatoExpression)))
              # element = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='email']")))
              return element
          except Exception as e:
              raise e
  if __name__ == '__main__':
      from selenium import webdriver
      driver = webdriver.Chrome()
      driver.get("http://mail.126.com")
      waitUtil = WaitUtil(driver)
      waitUtil.frame_available_and_switch_to_it("xpath","//iframe[contains(@id,'x-URS-iframe')]")
      e = waitUtil.visibility_element_located("xpath","//input[@name ='email']")
      e.send_keys("success")
      driver.quit()
      '''

    def presenceOfElementLocated(self,locatorMethod,locatorExpression,*arg):
        #显示等待页面元素出现,但是并一定可见，则返回该页面元素对象
        try:
            # if self.locationTypeDict.has_key(locatorMethod.lower()):
            if locatorMethod.lower() in self.locationTypeDict:
                self.wait.until(
                    EC.presence_of_element_located((
                        self.locationTypeDict[locatorMethod.lower()],
                        locatorExpression)))
                return
            else:
                raise TypeError("未找到定位元素，请确认定位方式是否正确")

        except Exception as e:
            raise e 


    def frameToBeAvailableAndSwitchToIt(self,locationType,locatorExpression,*arg):
        #检查frame是否存在 存在则切换进frame空间中
        try:
            self.wait.until(
                EC.frame_to_be_available_and_switch_to_it((
                    self.locationTypeDict[locationType.lower()],
                        locatorExpression)))
        except Exception as e:
            #抛出异常信息给上层调用者
            raise e

    def visibilityOfElementLocated(self,locationType,locatorExpression,*arg):
        #显示等待页面元素出现DOM中 并且可见，存在则返回该页面元素对象中
        try:
            self.wait.until(
                EC.visibility_of_element_located((self.locationTypeDict[locationType.lower()],locatorExpression )))
        except Exception as e:
            raise e

if __name__ =='__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://mail.126.com")
    WaitUtil = WaitUtil(driver)
    WaitUtil.frameToBeAvailableAndSwitchToIt("xpath","//iframe[contains(@id,'x-URS-iframe')]")
    print(WaitUtil.frameToBeAvailableAndSwitchToIt)
    WaitUtil.visibilityOfElementLocated("xpath","//input[@name ='email']")
    WaitUtil.presenceOfElementLocated("xpath","//input[@name ='email']")
    driver.quit()

