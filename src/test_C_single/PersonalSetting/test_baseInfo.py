#coding=utf-8
import unittest
from common.common import rq_baseInfo
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf

class Test_baseInfo(ParametrizedTestCase):
    u''' params domain '''
    def test_a(self):
        u''' correct domain '''
        response = rq_baseInfo(self.param,domain=getConf("constant","url").split("//")[1])
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_b(self):
        u''' no domain '''
        response = rq_baseInfo(self.param)
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_c(self):
        u''' wrong domain '''
        response = rq_baseInfo(self.param,domain="novaicare.com")
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_baseInfo()
    a.test_a()
    a.test_b()
    a.test_c()
