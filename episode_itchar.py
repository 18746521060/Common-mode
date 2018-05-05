#!/usr/bin/python3

# 今天研究了一下 itchar 接口，写下了一个自动发送给微信好友消息的
# 例子。算是额外的插曲
# itchat 定期给微信中某人发送金山词霸每日一句

import itchat
import requests
import json

# 判断是否为第一次运行该脚本
run_time = 1


def get_news():
    url = "http://open.iciba.com/dsapi"
    r = requests.get(url)
    english = r.json()["content"]
    china = r.json()["note"]
    tran = r.json()["translation"]
    return (english, china, tran)


def send_news(name):
    global run_time
    known = ""
    try:
        itchat.auto_login(hotReload=True)
        if run_time == 1:
            itchat.get_friends(update=True)
            run_time += 1
        my_friend = itchat.search_friends(name=name)
        known = my_friend[0]["UserName"]
        eng, chi, tra = get_news()
        message1 = str(eng)
        message2 = str(chi)
        message3 = str(tra)
        message4 = "来自关心你的人"
        # 发送消息
        itchat.send(message1, toUserName=known)
        itchat.send(message2, toUserName=known)
        itchat.send(message3, toUserName=known)
        itchat.send(message4, toUserName=known)
    except Exception as e:
        print("error:", e)
        message = u"hello welcome you"
        itchat.send(message, toUserName=known)


'''
# 这是我用面向对象的一种写法
class NotFoundFriend(Exception):
    """
    定义没发现好友的异常类
    """

    def __init__(self, date):
        super(NotFoundFriend, self).__init__(date)


class Event:
    def __init__(self):
        self.log_in()
        self.friend = None

    @classmethod
    def log_in(cls):
        """账号登录"""
        itchat.auto_login(hotReload=True)

    def set_friend(self, name):
        """ name 为您微信好友的备注名"""
        search_name = itchat.search_friends(name=name)
        if search_name:
            self.friend = search_name[0]["UserName"]
        else:
            raise NotFoundFriend("您没有该好友")

    def send_data(self, data):
        if self.friend:
            if isinstance(data, str):
                itchat.send(data, toUserName=self.friend)
            elif isinstance(data, bytes):
                itchat.send(data.decode("utf-8", errors="ignore"), toUserName=self.friend)
            else:
                itchat.send(json.loads(data), toUserName=self.friend)
        else:
            print("您还没有指定发送对象，我不知道发送给谁啊0_0...")

    def update_friend(self):
        """获取更新您的所有好友信息"""
        itchat.get_friends(update=True)
        
if __name__ == "__main__":
    eng, chi, tra = get_news()
    event = Event()
    event.set_friend(name="小明")
    event.send_data(eng)
    event.send_data(chi)
    event.send_data(tra)
'''

if __name__ == "__main__":
    name = input("Hello. Select the user name in your friends:")
    send_news(name)
