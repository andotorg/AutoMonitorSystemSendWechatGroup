# -*- coding: UTF-8 -*-
import datetime

def wxSendMsg(bot, imgs, msgs):
    #my_friend = bot.friends().search(u'FireU0')[0]
    my_group = bot.groups().search(u'系统部')[0] #FireU0
    #my_friend.send(u'你好啊')
    nowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for i in range(len(msgs)):
        my_group.send(msgs[i])
    for i in range(len(imgs)):
        my_group.send_image(imgs[i])
