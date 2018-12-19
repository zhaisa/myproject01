from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
dr = webdriver.Firefox(firefox_binary=binary)
    # dr.get('https://www.baidu.com')
    # elem = dr.find_element_by_name('wd')
    # elem.send_keys('seleniumhq' + Keys.RETURN)
    #
    # time.sleep(1)
    #
    #
    # dr.quit()