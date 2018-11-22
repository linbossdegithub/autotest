#coding=utf-8
import unittest
from common.common import rq_cameraConfig
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf



class Test_cameraConfig(ParametrizedTestCase):
    u''' sid  camera_id '''
    def test_a(self):
        u''' 正确的sid camera_id1 '''
        response = rq_cameraConfig(self.param,sid=getConf("data","sid"),camera_id=getConf("data", "camera_id1"))
        print response
        u''' check '''
        self.assertTrue(response["status"]==100000 and response["data"]["userName"]==getConf("constant", "user_e") and response["data"]["password"]==getConf("constant", "password_e"), "this case is failed")
        
    def test_b(self):
        u''' 错误的sid 正确的camera_id1 '''
        response = rq_cameraConfig(self.param,sid="000000000",camera_id=getConf("data", "camera_id1"))
        print response
        u''' check '''
        self.assertTrue(response["status"]==100001, "this case is failed")
        
    def test_c(self):
        u''' 正确的sid 错误的camera_id '''
        response = rq_cameraConfig(self.param,sid=getConf("data","sid"),camera_id="1234")
        print response
        u''' check '''
        self.assertTrue(response["status"]==100000, "this case is failed")
        
    def test_d(self):
        u''' 正确的sid 不传camera_id '''
        response = rq_cameraConfig(self.param,sid=getConf("data","sid"))
        print response
        u''' check '''
        self.assertTrue(response["status"]==100000 and len(response["data"])==0, "this case is failed")
        
    def test_e(self):
        u''' 不传参 '''
        response = rq_cameraConfig(self.param)
        print response
        u''' check '''
        self.assertTrue(response["status"]==100000 and len(response["data"])==0, "this case is failed")
        
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_cameraConfig()
#     a.test_a()
#     a.test_b()
#     a.test_c()
#     a.test_d()
    a.test_e()