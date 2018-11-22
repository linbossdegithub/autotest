#coding=utf-8
import unittest

from common.common import rq_clearSetting
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf



class Test_clearSetting(ParametrizedTestCase):
    u''' 参数 sid '''
    def test_a(self):
        u''' 正确的sid '''
        response = rq_clearSetting(self.param,sid=getConf("data","sid"))
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, "this case is failed")
        
    def test_b(self):
        u''' 错误的sid '''
        response = rq_clearSetting(self.param,sid='abdced')
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, "this case is failed")
        
    def test_c(self):
        u''' 不传sid '''
        response = rq_clearSetting(self.param,)
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, "this case is failed")
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_clearSetting()
    a.test_c()
