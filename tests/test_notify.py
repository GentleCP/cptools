#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-----------------File Info-----------------------
            Name: test_notify.py
            Description:
            Author: GentleCP
            Email: 574881148@qq.com
            WebSite: https://www.gentlecp.com
            Create Date: 2021/4/6 
-----------------End-----------------------------
"""
import pytest
from cptools.notify import ServerChan, DingDing, EmailSender

class TestServerChan(object):
    sc = ServerChan(token='')  # 请输入ServerChan的key进行测试
    def test_send_text(self):
        if self.sc.token.startswith('SCU'):
            assert self.sc.send_text(text='hello world') == True
        else:
            assert self.sc.send_text(title='hello world') == True

class TestDingDing(object):
    dd = DingDing(token='')  # 请输入DingDing的webhook assess_token进行测试

    def test_send_text(self):
        assert self.dd.send_text(text='【通知】hello world') == True

class TestEmail(object):
    sender = EmailSender(user='', password_or_auth_code='', host='')

    def test_send_text(self):
        assert self.sender.send_text(text='hello world', to=['574881148@qq.com']) == True


# if __name__ =='__main__':
#     pytest.main()