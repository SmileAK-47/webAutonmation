#enconding = utf -8
from action.PageAction import *
from util.WaitUtil import WaitUtil

import  time
def TestSendMailWithAttachment():
    print("启动浏览器")
    open_browser('chrome')
    maximize_brower()
    print("访问登录126邮箱页面")
    visit_url("https://mail.126.com/")
    time.sleep(2)
    assert_string_in_pagesource(u"你的专业电子邮局")
    print(u"访问126登录页面成功")
    time.sleep(3)
    waitFrameToBeAvailableAndSwitchToIt("xpath","//iframe[contains(@id,'x-URS-iframe')]")
    print("输入登录名")
    input_string("xpath","//input[@name='email']","sunsmileak007")
    print("输入登录密码")
    input_string("xpath","//input[@name='password']","wgwgwg0051")
    click("id","dologin")
    time.sleep(3)
    assert_title(u"网易邮箱")
    print("登录成功")
    waitVisibilityOfElementLocated("xpath","//span[text()= '写 信']")
    click("xpath","//span[text()= '写 信']")
    print("开始写信")
    print("输入收件人地址")
    input_string("xpath","//div[contains(@id ,'_mail_emailinput')]/input","125081306@qq.com")
    print("输入邮件主题")
    input_string("xpath","//div[@aria-label='邮件主题输入框，请输入邮件主题']/input",'带附件的邮件')
    print("单击上传单击附件按钮")
    click("xpath","//div[@title ='点击添加附件']")
    time.sleep(3)
    print("上传附件")
    paste_string(r"G:\KeyWordFromeWork\a.txt")
    press_enter_key()
    #切入iframe
    waitFrameToBeAvailableAndSwitchToIt("xpath","//iframe[@tabindex= '1']")
    print("进入iframe")
    print("写入邮件正文")
    input_string("xpath","//body[@class='nui-scroll']","正文写给ssssssssss")
    #切出iframe
    switch_to_default_content()
    print("退出")
    print("写信完成")
    print("开始发送邮件")
    click("xpath","//span[text()= '发送']")
    time.sleep(3)
    assert_string_in_pagesource("发送成功")
    # print(assert_string_in_pagesource("asdf 功"))
    print("邮件发送成功")
    close_browser()

if __name__ == "__main__":
    TestSendMailWithAttachment()