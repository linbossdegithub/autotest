#coding=utf-8
import unittest
from common.common import rq_cameraSetting
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_cameraSetting(ParametrizedTestCase):
    u'''  clearPeriod  isOpenDetection  sid '''  
    def test_a(self):
        u''' 正确的 clearPeriod isOpenDetetion sid ''' 
        response = rq_cameraSetting(self.param,sid=getConf("data","sid"),isOpenDetetion=0,clearPeriod=0)
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, "this case is failed")
        
    def test_b(self):
        u''' 错误的clearPeriod  isOpenDetetion 正确的sid '''
        response = rq_cameraSetting(self.param,sid=getConf("data","sid"),isOpenDetetion=7,clearPeriod=7)
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, "this case is failed")
        
    def test_c(self):
        u''' 错误的clearPeriod  isOpenDetetion 正确的sid '''
        response = rq_cameraSetting(self.param,sid="abcd",isOpenDetetion=0,clearPeriod=0)
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, "this case is failed")
        
        
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_cameraSetting()
    a.test_a()
    a.test_b()
    a.test_c()
