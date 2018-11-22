#coding=utf-8
import unittest

import requests

from common.common import rq_getScreenInfoBySid
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_getScreenInfoBySid(ParametrizedTestCase):
    u''' sid '''
       
    def test_a(self):
        u''' correct sid '''
        response = rq_getScreenInfoBySid(self.param,sid=getConf('data','sid'))
        print response
        u''' check '''
        self.assertTrue(response['status']==100000 and len(response['data']['screenInfo'])!=0, 'this case is failed')
       
    def test_b(self):
        u''' wrong sid '''
        response = rq_getScreenInfoBySid(self.param,sid='00000')
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_getScreenInfoBySid()
    a.test_a()
    a.test_b()

