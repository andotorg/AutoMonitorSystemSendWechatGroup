# -*- coding:utf8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from wxpy import *
import os
import datetime
import threading
import wxUtil
import urllib3
import requests
import json

nameArr = ["1.png",
               "2.png",
               "3.png"]

def capture():
    urlArr = ["https://andot.org",
              "https://andot.org",
              "https://andot.org"]

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')  # 上面三行代码就是为了将Chrome不弹出界面，实现无界面爬取

    driver1 = webdriver.Chrome(executable_path='D:\\InstallApp\\PythonLib\\chromedriver.exe',
                               chrome_options=chrome_options)  # .PhantomJS(executable_path='D:\\InstallApp\\PythonLib\\phantomjs-2.1.1-windows\\bin\\phantomjs')
    driver1.set_window_size(480, 1000)
    for i in range(len(urlArr)):
        driver1.get(urlArr[i])
        driver1.set_page_load_timeout(10000)
        data = driver1.title
        driver1.save_screenshot(nameArr[i])  # C:\\Users\\Andot\\Desktop\\andot-" + date + "
        print(data)
        print(os.getcwd())

def getGudingTime():
    # 获取现在时间
    now_time = datetime.datetime.now()
    # 获取明天时间
    next_time = now_time + datetime.timedelta(days=+0)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    # 获取明天3点时间
    next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 07:15:00",
                                           "%Y-%m-%d %H:%M:%S")
    # # 获取昨天时间
    # last_time = now_time + datetime.timedelta(days=-1)

    # 获取距离明天3点时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()
    print(timer_start_time)
    return timer_start_time;

def getWarn():
    url = "https://andot.org"
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
    print("请注意目前有%d个告警" % warn)
    return "请注意目前有%d个告警" % warn


def hello(bot):
    print("定时器开始于 %s\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    msgArr = ["运维时间： %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), getWarn()];
    capture()
    wxUtil.wxSendMsg(bot, nameArr, msgArr)

    global timer
    #timer = threading.Timer(startTime, hello)
    #timer.start()

bot = Bot()
startTime = getGudingTime()
timer = threading.Timer(startTime, hello, [bot]) #, [startTime]
timer.start()