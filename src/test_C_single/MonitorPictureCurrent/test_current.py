#coding=utf-8
import unittest
from common.common import rq_current
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_current(ParametrizedTestCase):
    u''' sid  camerId '''
    def test_a(self):
        u'''正确的sid 和 camerId1'''
        response = rq_current(self.param,sid=getConf("data","sid"),cameraId=getConf("data", "camera_id1"))
        print response
        u''' check '''
        self.assertTrue(response["status"]==100000 and len(response["data"])!=0, "this case is failed")
        
    def test_b(self):
        u'''正确的sid 和 camerId2'''
        response = rq_current(self.param,sid=getConf("data","sid"),cameraId=getConf("data", "camera_id2"))
        print response
        u''' check '''
        self.assertTrue(response["status"]==100000 and len(response["data"])!=0, "this case is failed")
        
    def test_c(self):
        u'''正确的sid 和 camerId3'''
        response = rq_current(self.param,sid=getConf("data","sid"),cameraId=getConf("data", "camera_id3"))
        print response
        u''' check '''
        self.assertTrue(response["status"]==100000 and len(response["data"])!=0, "this case is failed")
        
    def test_d(self):
        u'''正确的sid 和 camerId4'''
        response = rq_current(self.param,sid=getConf("data","sid"),cameraId=getConf("data", "camera_id4"))
        print response
        u''' check '''
        self.assertTrue(response["status"]==100000 and len(response["data"])!=0, "this case is failed")
    
    def test_e(self):
        u'''正确的sid 和 错误的cameraId'''
        response = rq_current(self.param,sid=getConf("data","sid"),cameraId="adb")
        print response
        u''' check '''
        self.assertTrue(response["status"]==100000 and len(response["data"])==0, "this case is failed")
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_current()
#     a.test_a()
#     a.test_b()
#     a.test_c()
    a.test_d()
    a.test_e()
