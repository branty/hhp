#-*- coding:utf-8 -*-

"""
Author: Wang, Jun
Email: wangjun41@baidu.com
Date: 2018-11-16 
"""

import os

from django.core.wsgi import get_wsgi_application
from upload.utils import eam_log

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

eam_log.InitLog("hhproject.log")
application = get_wsgi_application()
