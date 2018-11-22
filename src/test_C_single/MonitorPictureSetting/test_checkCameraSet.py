#coding=utf-8
import unittest

from common.common import rq_checkCameraSet
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf



class Test_checkCameraSet(ParametrizedTestCase):
    u''' 参数 sid  camera_id '''
    def test_a(self):
        u''' 正确的 sid camera_id'''
        response = rq_checkCameraSet(self.param,sid=getConf("data","sid"),camera_id=getConf("data", "camera_id1"))
        print response
        u''' check '''
        self.assertTrue(response['status']==100000 and response['data']['code']==0, "this case is failed")
        
    def test_b(self):
        u''' 不传sid '''
        response = rq_checkCameraSet(self.param,camera_id=getConf("data", "camera_id1"))
        print response
        u''' check '''
        self.assertTrue(response['status']==100001 , "this case is failed")
        
    def test_c(self):
        u''' 不传camera_id '''
        response = rq_checkCameraSet(self.param,sid=getConf("data","sid"))
        print response
        u''' check '''
        self.assertTrue(response['status']==100000 , "this case is failed")
        
    def test_d(self):
        u''' 错误的camera_id '''
        response = rq_checkCameraSet(self.param,sid=getConf("data","sid"),camera_id="abdc")
        print response
        u''' check '''
        self.assertTrue(response['status']==100000 , "this case is failed")
        
        
        
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_checkCameraSet()
    a.test_d()
