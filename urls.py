#-*- coding:utf-8 -*-

"""
Author: Wang, Jun
Email: wangjun41@baidu.com
Date: 2018-11-16 
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from upload import urls as upload_urls

ROOT_URL = "hhp"

urlpatterns = [
    url(r'^%s/' % ROOT_URL, include(upload_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

