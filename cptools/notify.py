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


