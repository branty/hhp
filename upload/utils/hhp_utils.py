#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
Author: Wang, Jun
Email: wangjun41@baidu.com
Date: 2018-11-16 
"""
import json

from django.http import HttpResponse


def http_response(func):
    """A decorate function to convert str message into http response
    """
    def decorator(request, *args, **kwargs):
        """response decorator.

        :param request: http request from user
        """    
        message = func(request, *args, **kwargs)
        return HttpResponse(json.dumps(message), content_type="application/json")

    return decorator
