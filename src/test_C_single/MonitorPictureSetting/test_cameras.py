#coding=utf-8
import unittest
from common.common import rq_cameras
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_cameras(ParametrizedTestCase):
    u''' sid '''
       
    def test_a(self):
        u'''正确的sid'''
        response = rq_cameras(self.param,sid=getConf("data","sid"))
        print response
        u''' check '''
        self.assertTrue(response["status"]==100000 and len(response["data"])==4, "this case is failed")
       
    def test_b(self):
        u'''错误的sid'''
        response = rq_cameras(self.param,sid="0000000")
        print response
        u''' check '''
        self.assertTrue(response["status"]==100001, "this case is failed")
       
    def test_c(self):
        u'''不传参'''
        response = rq_cameras(self.param,)
        print response
        u''' check '''
        self.assertTrue(response["status"]==100001, "this case is failed")
        
        
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_cameras()
    a.test_a()
    a.test_b()
    a.test_c()
    
    