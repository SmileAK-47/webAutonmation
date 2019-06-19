# encoding = utf -8
# 定义整个框架中所需要的一些全局常亮值，
import os

# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(parentDirPath)
#cookie路径
# cookiePath=parentDirPath+"\\config\\add_cookie.txt"

# 异常截图存放目录绝对路径
screenPicturesDir = parentDirPath + "\\exceptionpicutres\\"

# 测试数据文件存放绝对路径
dataFilePath = parentDirPath + "\\testData\\126邮箱发送邮件.xlsx"

ieDriverFilePath = parentDirPath + "\\IEDriverServer.exe"
chromeDriverFilePath = parentDirPath + "\\chromedriver.exe"
firefoxDriverFilePath = parentDirPath + "\\geckodriver.exe"

# 测试数据文件中，测试用例表中部分列对应的数字序号
testCase_testCaseName = 2
testCase_testStepSheetName = 4
testCase_isExecute = 5
testCase_runTime = 6
testCase_testResult = 7

# 用例步骤表中，部分对应的数字序号
testStep_testStepDescribe = 2
testStep_keyWords = 3
testStep_locationType = 4
testStep_locatorExpression = 5
testStep_operateValue = 6
testStep_runTime = 7
testStep_testResult = 8
testStep_errorInfo = 9
testStep_errorPic = 10

# 数据表源中，是否执行列对应的数字编号
dataSource_isExecute = 7
dataSource_email = 3
dataSource_runTime = 8
dataSource_result = 9
