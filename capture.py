#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2018/10/3 23:11
#@Author: andot
#@File  : capture.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import urllib3
import requests
import json

def capture(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')  # 上面三行代码就是为了将Chrome不弹出界面，实现无界面爬取

    driver1 = webdriver.Chrome(executable_path='D:\\InstallApp\\PythonLib\\chromedriver.exe')  # .PhantomJS(executable_path='D:\\InstallApp\\PythonLib\\phantomjs-2.1.1-windows\\bin\\phantomjs')
    driver1.set_window_size(480, 1000)
    driver1.get(url)
    driver1.set_page_load_timeout(10000)
    data = driver1.title
    driver1.save_screenshot("aa.png")  # C:\\Users\\Andot\\Desktop\\andot-" + date + "
    print(data)
    print(os.getcwd())


def getWarn():
    url = "http://baidu.com"
    #  忽略警告：InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
    requests.packages.urllib3.disable_warnings()
    # 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
    http = urllib3.PoolManager()
    # 通过request()方法创建一个请求：
    r = http.request('GET', url)
    print(r.status)  # 200
    # 获得html源码,utf-8解码
    data = r.data.decode()
    warn = json.loads(data)["warn"]
    print("请注意目前有%d个长期告警" % warn)

#capture("http://jngffp.cn/m/mobileHisTop10.jsp?regionId=284&regionType=2")

getWarn()