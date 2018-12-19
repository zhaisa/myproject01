
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import urllib.request
import re

url = 'http://testhf.irongbei.com'

binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary)
driver.get(url)
time.sleep(1)
driver.maximize_window()
# 将浏览器最大化
driver.refresh()
driver.find_element_by_link_text("登录").click()
time.sleep(1)
driver.find_element_by_id("user_name").send_keys("17409040211")
driver.find_element_by_id("user_password").send_keys("123456")
driver.find_element_by_id("qianlogin").click()
time.sleep(1)
driver.get('http://testhf.irongbei.com/index/pdetail?id=13307')
time.sleep(1)
driver.find_element_by_id("invest_account").send_keys("100")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[2]/div/div[5]/div/img").click()
time.sleep(1)

driver.find_element_by_link_text("立即出借").click()

driver.find_element_by_class_name("magBtn").click()
time.sleep(4)
'''handleb = driver.current_window_handle  # 获取当前页，当前页面B赋给handleb
sreach_windows = driver.window_handles  # 将当前所有handle放入列表中


新建newhandle为search_windows内的元素
判断newhandle是不是页面A如果不是就定位到newhandle
也就是页面B

for newhandle in sreach_windows:
    if (newhandle != handlea):
        driver.switch_to_window(newhandle)
        h_title = driver.find_element_by_xpath("//h1/span[3]")  # 定位页面B中的h1内的标题名称
        print(h_title.text)
        # 断言文字是否匹配，如果匹配则pass，否则fail
        try:
            assert atxt == h_title.text
            print("pass")
        except Exception as e:
            print("fail")

        这是最关键的一步，在这里必须关闭新的页面，及页面B
        否则在循环遍历中或出现疯狂打开新页面的情况
        所以必须用close方法关闭窗口

        driver.close()
        driver.switch_to_window(sreach_windows[0])  # 重新定位到页面A
time.sleep(1)
'''
sreach_window = driver.current_window_handle  # 此行代码用来定位当前页面

driver.find_element_by_id("pass").send_keys("921019")
driver.find_element_by_id("sub").click()