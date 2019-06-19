#conding = utf - 8
from selenium import webdriver
import json
import time
#正常登陆一次获取cookie ***** 一定要选择保存密码*****
def login_cookie():
    browser = webdriver.Chrome(r'D:\coed\automation\web_ShiYue\KeyWordFromeWork-master\chromedriver.exe')
    browser.set_page_load_timeout(20)
    browser.set_script_timeout(20)
    try:
        browser.get("https://www.126.com/")
    except:
        browser.execute_script("window.stop()")
    time.sleep(5)
    input("请登陆后按Enter")
    cookies = browser.get_cookies()
    print("cookies",cookies)
    jsonCookies = json.dumps(cookies)
    with open('cookies6.11.01.txt', 'w') as f:   #可自定义文件路径默认当前文件路径
        f.write(jsonCookies)
    # print(browser.get_cookies())
    time.sleep(5)
    browser.quit()
    return cookies

def new_browser():
    browser = webdriver.Chrome(r'D:\coed\automation\web_ShiYue\KeyWordFromeWork-master\chromedriver.exe')
    browser.delete_all_cookies() #清除所有cookie
    browser.set_page_load_timeout(20)
    browser.set_script_timeout(20)
    try:
        browser.get("https://www.126.com/")
    except:
        browser.execute_script("window.stop()")
    time.sleep(5)
    f1 = open('cookies6.11.01.txt')
    cookies = f1.read()
    cookies = json.loads(cookies)
    #添加cookie到未登的录页面
    for co in cookies:
        browser.add_cookie(co)
    browser.refresh() #再次刷新页面则得到登陆后的界面
    time.sleep(5)
    browser.close()

if __name__ =="__main__":
    # login_cookie()
    new_browser()

