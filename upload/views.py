#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
Author: Wang, Jun
Email: wangjun41@baidu.com
Date: 2018-11-16 
"""

from itertools import chain
import json
import StringIO
import sys

from django import forms
from xlwt import Workbook

from upload import exceptions
from upload.utils import eam_log as log
from upload.utils.hhp_utils import http_response

reload(sys)
sys.setdefaultencoding('utf-8')
LOG = log.logger(__name__)
SUCCESS_MSG = 'success'
FAILURE_MSG = 'failure'

class UploadFileForm(forms.Form):
    file = forms.FileField()


class ValidRequestPramaters(object):
    """valid upload request parameters"""
    # business category
    BUSINESS = 'business'
    # query period for recent items
    PERIOD = 'period'
    # loan pattern
    PATTERN = 'pattern'
    # the usage for loan pattern
    USAGE = 'usage'

QUERY_ENUMS = {
    '所属机构': 'organization',
    '业务种类': 'business',
    '姓户名称': 'name',
    '合同金额': 'total',
    '发放日期': 'release_time',
    '到期时间': 'expiration',
    '发放金额': 'amount',
    '贷款余额': 'balance',
    '利率_千分之': 'ratio_per_thousand',
    '逾期利率_千分之': 'overdue_per_thound',
    '表内欠息金额': 'debit_inside',
    '表外欠息金额': 'debit_outside',
    '是否贴息': 'ratio_allowance',
    '账户状态': 'status',
    '贷款形态（五级）': 'pattern',
    '主办客户经理': 'manager',
    '贷款用途': 'usage'
}


PARAMS = filter(lambda key: not key.startswith('_') ,vars(ValidRequestPramaters).keys()) 

def check_request_paras(func):
    def _decorate(request, *args, **kwargs):
        message = {
            'success': True,
            'message': SUCCESS_MSG,
            'data': ''
        }
        query_keys = request.GET.keys() 
        for key in query_keys:
            if key not in PARAMS:
                msg = '请求参数%s，值为(%s)不支持, 请重新输入' % (key, request.GET.get(key))
                LOG.error(msg)
                message['success'] = False
                message['message'] = msg
                return message
        return func(request, *args, **kwargs)
    return _decorate
    

def parse_excel(request):
    """prase excel

    :param request: request.
    :param asset: asset type
    """
    body = dict()
    if request.method.lower() == "post":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            rows = request.FILES['file'].get_sheet().to_array()
            keys =  rows[0]
            #TODO
        else:
            raise exceptions.ExcelFormError('上传的的文件属于非法excel,请重新上传')
    

@http_response
@check_request_paras
def upload(request):
    """receive excel from request and then parse it

    :param request: request.
    """
    message = {
        'success': True,
        'message': SUCCESS_MSG,
        'data': ''
    }
    try:
        response = parse_excel(request)
        message['success'] = json.loads(response.content).get('success')
        message['message'] = json.loads(response.content).get('message')
        message['data'] = json.loads(response.content).get('data')
    except exceptions.UnsupportedError as e:
        LOG.error(e)
        message['success'] = False
        message['message'] = e.msg
    except exceptions.ExcelFormError as e:
        LOG.error(e)
        message['success'] = False
        message['message'] = e.msg
    except Exception as e:
        LOG.error(e)
        message['success'] = False
        message['message'] = e.message
    return message
