#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Log handler
This module provides a log handler which helps developer process log easily.

Examples:
    >>> from cptools import LogHandler
    >>> logger = LogHandler(name='test')
    >>> logger.info('hello')

"""

import os
import logging

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path

from logging.handlers import TimedRotatingFileHandler

# 日志级别
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0


class LogHandler(logging.Logger):
    """LogHandler
    """

    def __init__(self, name: str = '', level: int = INFO, stream: bool = True, file: bool = False,
                 log_path: str = './log'):
        """Initialize log handler
        Args:
            name: logger name
            level: log level, default: INFO
            stream: print log to stdout
            file: print log to file
            log_path: where to save log, default: `./log`
        """
        self.name = name if name else self.__class__.__name__
        self._level = level
        self._log_path = Path(log_path)
        if file and not self._log_path.exists():
            os.makedirs(str(self._log_path))
        logging.Logger.__init__(self, self.name, level=self._level)
        if stream:
            self.__setStreamHandler__()
        # if file and platform.system() != "Windows":
        if file:
            self.__setFileHandler__()

    @property
    def log_path(self):
        return self._log_path

    def __setFileHandler__(self, level=None):
        """
        set file handler
        :param level:
        :return:
        """
        file_path = self._log_path.joinpath('{name}.log'.format(name=self.name))
        # 设置日志回滚, 保存在log目录, 一天保存一个文件, 保留15天
        file_handler = TimedRotatingFileHandler(filename=str(file_path), when='D', interval=1, backupCount=15)
        file_handler.suffix = '%Y%m%d.log'
        if not level:
            file_handler.setLevel(self._level)
        else:
            file_handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s %(filename)s-line:%(lineno)d <%(name)s> [%(levelname)s] %(message)s')

        file_handler.setFormatter(formatter)
        self.file_handler = file_handler
        self.addHandler(file_handler)

    def __setStreamHandler__(self, level=None):
        """
        set stream handler
        :param level:
        :return:
        """
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(filename)s-line:%(lineno)d <%(name)s> [%(levelname)s] %(message)s')
        stream_handler.setFormatter(formatter)
        if not level:
            stream_handler.setLevel(self._level)
        else:
            stream_handler.setLevel(level)
        self.addHandler(stream_handler)
