# coding=utf-8
import unittest
from ftplib import FTP

import datetime
from flask import json
import requests

from common.common import rq_getDeviceInfo, rq_cameraConfig, rq_realTime, rq_saveClientReportParamaterSet, \
    rq_saveReportScreenSet, rq_reportSetList, rq_deleteSetup, rq_getScreenInfoBySid
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf,setConf


class Test_bug3(ParametrizedTestCase):
    def test_a(self):
        u''' 验证屏体邮箱默认语言为中文 '''
        print getConf("data","sid")
        result = rq_getScreenInfoBySid(self.param,sid = getConf("data","sid"))

        a = result["data"]["emailConf"]["emailLanguage"]

        u''' check'''
        self.assertTrue(str(a) == "1", 'this case is failed')







