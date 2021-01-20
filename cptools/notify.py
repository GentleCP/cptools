#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
-----------------File Info-----------------------
            Name: notify.py
            Description:
            Author: GentleCP
            Email: 574881148@qq.com
            WebSite: https://www.gentlecp.com
            Create Date: 2020-12-29 
-----------------End-----------------------------
"""

import os
import requests
from abc import abstractmethod, ABCMeta

import yagmail
import smtplib
from dingtalkchatbot.chatbot import DingtalkChatbot


def mac_notify(title,text):
    """
    use mac default notify
    :param title: notify title
    :param text: notify text
    :return: None
    """
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


class Notifier(object):
    """
    base notifier
    """

    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        pass


    @abstractmethod
    def send_text(self, text):
        pass


class ServerChan(Notifier):
    """
    Server酱，需要提供key
    """

    def __init__(self, token=None, *args, **kwargs):
        super(ServerChan, self).__init__(*args, **kwargs)
        self._token = token
        self.__api = "https://sc.ftqq.com/{}.send?text={}"


    @property
    def token(self):
        return self._token


    @token.setter
    def token(self, token):
        self._token = token


    def send_text(self, text):
        '''
        请求结果：
            成功：{'dataset': 'done', 'errmsg': 'success', 'errno': 0}
            短时间内重复发送：{'errmsg': '不要重复发送同样的内容', 'errno': 1024}
            失败：{"errno":1024,"errmsg":"bad pushtoken"}
        :param text:
        :return:
        '''
        res = requests.get(url=self.__api.format(self._token, text)).json()
        if res.get('errno') == 0:
            print("Server酱消息发送成功！")
            return True
        else:
            print("Server酱消息发送失败，原因：{}".format(res.get('errmsg')))
            return False


class DingDing(Notifier):
    """
    钉钉机器人推送
    """

    def __init__(self, token=None, *args, **kwargs):
        super(DingDing, self).__init__(*args, **kwargs)
        self._token = token
        if self._token:
            self.__webhook = "https://oapi.dingtalk.com/robot/send?access_token={}".format(self._token)
            self._dd = DingtalkChatbot(webhook=self.__webhook)


    @property
    def token(self):
        return self._token


    @token.setter
    def token(self, token):
        self._token = token
        self.__webhook = "https://oapi.dingtalk.com/robot/send?access_token={}".format(self._token)
        self._dd = DingtalkChatbot(webhook=self.__webhook)


    def send_text(self, text):
        '''
        钉钉如果有关键字要求，需要在内容中包含关键字
        请求结果：
            成功：{'errcode': 0, 'errmsg': 'ok'}
            失败：{'errmsg': 'token is not exist', 'errcode': 300001}
        :param text:
        :return:
        '''
        res = self._dd.send_text(msg=text)
        if res.get('errcode') == 0:
            print("DingDing消息发送成功！")
            return True
        else:
            print("DingDing消息发送失败，原因：{}".format(res.get('errmsg')))
            return False


class EmailSender(Notifier):
    """
    邮件发送通知
    """

    def __init__(self,
                 user=None,
                 password_or_auth_code=None,
                 host=None,
                 *args, **kwargs):
        '''
        user is the send user
        :param user:
        :param password_or_auth_code:
        :param host:
        :param args:
        :param kwargs:
        '''
        super(EmailSender, self).__init__(*args, **kwargs)
        self._user = user
        self._passwd_or_auth_code = password_or_auth_code
        self._host = host
        self.__yag = yagmail.SMTP(user=self._user, password=self._passwd_or_auth_code, host=self._host)


    def send_text(self, text, contents='', to=[]):
        '''
        send text by email, it could be send to multi people
        :param text:
        :param contents:
        :param to: who to send, one email address for one person
        :return: send result
        '''
        try:
            to = to if not to else [self._user]  # 如果没有填入收件人，默认发送给自己
            self.__yag.send(to=to, subject=text, contents=contents)
        except smtplib.SMTPAuthenticationError:
            print("send mail error, please check your password or auth code.")



def test_email(cfg):
    email = EmailSender(user=cfg.get('Email','user'),
                        password_or_auth_code=cfg.get('Email','passwd'),
                        host=cfg.get('Email', 'host'))
    email.send_text(text='test', contents='this is a test mail', to=['m17713549835@163.com'])


def test_ServerChan(cfg):
    SJ = ServerChan()
    SJ.token=cfg.get('ServerChan', 'token')
    SJ.send_text(text='This is a test.')


def test_DingDing(cfg):
    dd = DingDing()
    dd.token = cfg.get('DingDing', 'token')
    dd.send_text(text='【通知】This is a test')  # 钉钉如果有关键字，自己添加测试的关键字


from configparser import ConfigParser

if __name__ == "__main__":
    cfg = ConfigParser()
    cfg.read('config.ini',encoding='utf-8')
    # test_email(cfg)
    # test_ServerChan(cfg)
    # test_DingDing(cfg)
    mac_notify(title='Warning', text='This is a test')