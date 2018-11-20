#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
Author: Wang, Jun
Email: wangjun41@baidu.com
Date: 2018-11-16 
"""

class BaseException(Exception):
    "base exception"
    def __init__(self, msg):
        self.msg = msg


class UnsupportedError(BaseException):
    """Not support"""
    def __init__(self, msg):
        self.msg = msg


class RequestMethodNotImplemented(UnsupportedError):
    """Request method not implemented"""
    def __init__(self, msg):
        self.msg = msg


class ParameterNotFound(BaseException):
    """Parameter not Found"""
    def __init__(self, msg):
        self.msg = msg
        

class ExcelFormError(BaseException):
    """Excel form is invalid"""
    def __init__(self, msg):
        self.msg = msg
        