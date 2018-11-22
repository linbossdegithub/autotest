#coding=utf-8
import unittest
from common.common import rq_getDeviceInfo
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf

class Test_getDeviceInfo(ParametrizedTestCase):
    def test_a(self):
        u''' correct sid '''
        r = self.param
        response = rq_getDeviceInfo(r,sid=getConf('data','sid'))
        print response 
        u''' check'''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    # def test_b(self):
    #     u''' no sid '''
    #     response = rq_getDeviceInfo()
    #     print response
    #     u''' check'''
    #     self.assertTrue(response['status']==100000, 'this case is failed')
    #
    # def test_c(self):
    #     u''' wrong sid '''
    #     response = rq_getDeviceInfo(sid='00000')
    #     print response
    #     u''' check'''
    #     self.assertTrue(response['status']==100000, 'this case is failed')
        
    def runTest(self):
        pass
        
if __name__ == '__main__':
    a = Test_getDeviceInfo()
    a.test_a()
    a.test_b()
    a.test_c()
    
