from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import urllib.request
import re
import os
listmy01=[]

def login():
    binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
    dr = webdriver.Firefox(firefox_binary=binary)
    dr.get("http://test-risk.irongbei.com/")
    time.sleep(1)
    dr.find_element_by_id('username').clear()
    dr.find_element_by_id('username').send_keys('hometest')
    dr.find_element_by_id('password').clear()
    dr.find_element_by_id('password').send_keys("123456")
    dr.find_element_by_id('verify').send_keys("8888")
    dr.find_element_by_id('login').click()

    time.sleep(2)
    dr.switch_to.frame("leftmenu")
    dr.find_element_by_tag_name("dt").click()
    url = dr.find_element_by_link_text("审核列表").get_attribute("href")
    dr.get(url)

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0")
    response = urllib.request.urlopen(url)
    html = response.read()
    print(html)


def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('<span class="laypage_curr" style="background-color:#4390b9">') + 60
    b = html.find('<', a)
    print(html[a:b])
    return html[a:b]
def find_ids(url):
    html = url_open(url).decode('utf-8')
    id_adds = []
    searchObj = re.search(r'<td>(.+?)</td>',html)  # 查找数字

    for i in searchObj:
        id_adds.append(searchObj.group(i))
    return id_adds
def save_ids(file,id_adds):
    for each in id_adds:
        listmy01.append(each)
    with open(file, 'wb') as f:
        f.write(each)


def download_id(file='mmm.txt', pages=10):
    url="http://test-risk.irongbei.com/homeloan/index.html"
    page_num = int(get_page(url))
    for i in range(pages):
        page_num += i
        page_url = url + '?p=' + str(page_num) + '&PHPSESSID=6203fukruhhk8q87u7o11jpfu5'
        id_adds= find_ids(page_url)
        save_ids(file,id_adds)



if __name__ == '__main__':
    login()
    download_id(file='mmm.txt', pages=10)


for i in listmy01:
    print(i)

