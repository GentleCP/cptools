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

class AuthError(Exception):
    pass

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
        self._check_configure()


    @abstractmethod
    def send_text(self, text):
        pass

    @abstractmethod
    def _check_configure(self):
        '''
        验证基本配置信息是否正确
        :return:
        '''
        pass

class ServerChan(Notifier):
    """
    Server酱，需要提供key
    """

    def __init__(self, token=None, *args, **kwargs):
        self._token = token
        self.__api = "https://sc.ftqq.com/{token}.send?text={text}&desp={desp}"
        self.__new_api = "https://sctapi.ftqq.com/{token}.send?title={title}&desp={desp}"
        super(ServerChan, self).__init__(*args, **kwargs)


    @property
    def token(self):
        return self._token


    @token.setter
    def token(self, token):
        self._token = token

    def _check_configure(self):
        if not self._token:
            raise AuthError('请设置ServerChan token')

    def send_text(self, text="", title="", desp=""):
        '''
        老接口(即将下线)请求结果：
            成功：{'dataset': 'done', 'errmsg': 'success', 'errno': 0}
            短时间内重复发送：{'errmsg': '不要重复发送同样的内容', 'errno': 1024}
            失败：{"errno":1024,"errmsg":"bad pushtoken"}

        新接口请求结果：
            成功：
                        {
              "code": 0,
              "message": "",
              "data": {
                "pushid": "1663686",
                "readkey": "SCTPmUPAz9ljk3Q",
                "error": "SUCCESS",
                "errno": 0
              }
            }
            失败：
                空title
                {
                  "message": "[INPUT]title 不能为空",
                  "code": 20001,
                  "info": "title 不能为空",
                  "args": [
                    null
                  ]
                }
                错误token
                {
                  "message": "[AUTH]用户不存在或者权限不足",
                  "code": 40001,
                  "info": "用户不存在或者权限不足",
                  "args": [
                    null
                  ]
                }
        :param text: 老接口的标题
        :param title: 新接口的标题
        :param desp: 描述信息，支持markdown
        :return:
        '''

        if self._token.startswith("SCU"):
            # old api
            print("你正在使用老版Server酱，该版本在21年4月底将失效，请尽快迁移到新版")
            res = requests.get(url=self.__api.format(token=self._token, text=text, desp=desp)).json()
            if res.get('errno') == 0:
                print("Server酱消息发送成功！")
                return True
            else:
                print("Server酱消息发送失败，原因：{}".format(res.get('errmsg')))
                return False
        else:
            # new api
            res = requests.get(url=self.__new_api.format(token=self._token, title=title, desp=desp)).json()
            if res.get('code') == 0:
                print("Server酱消息发送成功！")
                return True
            else:
                print("Server酱消息发送失败，原因：{}".format(res.get('info')))
                return False




class DingDing(Notifier):
    """
    钉钉机器人推送
    """

    def __init__(self, token=None, *args, **kwargs):
        self._token = token
        if self._token:
            self.__webhook = "https://oapi.dingtalk.com/robot/send?access_token={}".format(self._token)
            self._dd = DingtalkChatbot(webhook=self.__webhook)
        super(DingDing, self).__init__(*args, **kwargs)


    @property
    def token(self):
        return self._token


    @token.setter
    def token(self, token):
        self._token = token
        self.__webhook = "https://oapi.dingtalk.com/robot/send?access_token={}".format(self._token)
        self._dd = DingtalkChatbot(webhook=self.__webhook)

    def _check_configure(self):
        if not self._token:
            raise AuthError('请设置DingDing token')

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
        self._user = user
        self._passwd_or_auth_code = password_or_auth_code
        self._host = host
        self.__yag = yagmail.SMTP(user=self._user, password=self._passwd_or_auth_code, host=self._host)
        super(EmailSender, self).__init__(*args, **kwargs)

    def _check_configure(self):
        if not (self._user and self._passwd_or_auth_code and self._host):
            raise AuthError('请完整配置EmailSender信息')

    def send_text(self, text, contents='', to=[]):
        '''
        send text by email, it could be send to multi people
        :param text:
        :param contents:
        :param to: who to send, one email address for one person
        :return: send result
        '''
        try:
            to = to if to else [self._user]  # 如果没有填入收件人，默认发送给自己
            self.__yag.send(to=to, subject=text, contents=contents)
        except smtplib.SMTPAuthenticationError:
            print("send mail error, please check your password or auth code.")
            return False
        else:
            return True
