#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
Author: Wang, Jun
Email: wangjun41@baidu.com
Date: 2018-11-16 
"""

from django.views.generic import TemplateView
from django.conf.urls import url
from upload import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^upload$', views.upload, name='upload excel'),
]
