#!/usr/bin/env python
# -*- encoding=utf-8 -*-
# ################################################################################
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
This module provide log framework of eam

Authors: wangjun41@baidu.com
Date:    2018/11/16

"""

import logging.handlers

import settings

LOG_CONF =  settings.EAM_LOGGING

def get_log_conf(section, option, default=None):
    """Get log option from a section
    """
    try:
        conf = LOG_CONF[section][option]
        return conf
    except KeyError as e:
        if default is not None:
            return default
        else:
            raise KeyError(e)
     
ROOT_LEVEL = get_log_conf('logger_root', 'level')
LOG_FORMAT = get_log_conf('formatter_simpleFormatter', 'format')
DATE_FORMAT = get_log_conf('formatter_simpleFormatter', 'datefmt')
FILE_HANDLER_LEVEL = get_log_conf('handler_fileHandler', 'level')
FILE_HANDLER_PATH = get_log_conf('handler_fileHandler', 'path')
FILE_HANDLER_MODE = get_log_conf('handler_fileHandler', 'mode')
FILE_HANDLER_MAXBYTES = int(get_log_conf('handler_fileHandler', 'maxbytes'))
FILE_HANDLER_BACKUPCOUNT = int(get_log_conf('handler_fileHandler',
                                            'backupcount'))
CONSOLE_HANDLER_LEVEL = get_log_conf('handler_consoleHandler', 'level')


class ContextAdapter(object):
    """Log context Adapter
    """
    def __init__(self, logger):
        """constructor func
        """
        self.logger = logger

    def debug(self, msg):
        """debug func
        """
        if msg is not None:
            self.logger.debug(msg)

    def info(self, msg):
        """info func
        """
        if msg is not None:
            self.logger.info(msg)

    def warn(self, msg):
        """warn func
        """
        if msg is not None:
            self.logger.warn(msg)

    def error(self, msg):
        """error func
        """
        if msg is not None:
            self.logger.error(msg)

    def critical(self, msg):
        """critical func
        """
        if msg is not None:
            self.logger.critical(msg)


class RequestContextFilter(logging.Filter):
    """Demonstrate how to filter request content"""

    def filter(self, record):
        # The call signature matches string interpolation: args can be a tuple or a lone dict
        if record.args and isinstance(record.args, tuple):
            return not str(record.args[0]).startswith('Request is Coming')
        return True


_loggers = {}


def logger(name='unknown'):
    """logger func
    """
    if name not in _loggers:
        _loggers[name] = ContextAdapter(logging.getLogger(name))
    return _loggers[name]


def InitLog(file_name, log_name=None):
    """Initlog func
    """
    initlogger = logger(log_name).logger
    initlogger.setLevel(getattr(logging, ROOT_LEVEL))
    filepath = FILE_HANDLER_PATH + '/' + file_name
    formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    file_handler = logging.handlers.\
        RotatingFileHandler(filename=filepath,
                            maxBytes=FILE_HANDLER_MAXBYTES,
                            mode=FILE_HANDLER_MODE,
                            backupCount=FILE_HANDLER_BACKUPCOUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(getattr(logging, FILE_HANDLER_LEVEL))
    file_handler.addFilter(RequestContextFilter())
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, CONSOLE_HANDLER_LEVEL))
    console_handler.setFormatter(formatter)
    console_handler.addFilter(RequestContextFilter())
    initlogger.addHandler(file_handler)
    initlogger.addHandler(console_handler)