#!/usr/bin/env python2
#-*- coding:utf-8 -*-


"""
Author: Wang, Jun
Email: wangjun41@baidu.com
Date: 2018-11-16 
"""

import os
import sys

from upload.utils import eam_log

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eam.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    # init log module
    eam_log.InitLog("hhproject.log")
    execute_from_command_line(sys.argv)
    