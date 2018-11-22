#coding=utf-8
import unittest
from common.common import rq_enableSet
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf



class Test_enableSet(ParametrizedTestCase):
    u''' params  camera_id:7793  enable:false  sid:"4354" '''
       
    def test_a(self):
        u'''correct sid camera_id enable'''
        response = rq_enableSet(self.param,sid=getConf("data","sid"),camera_id=getConf('data', 'camera_id1'),enable=True)
        print response 
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
       
    def test_b(self):
        u'''wrong  sid , correct camera_id enable'''
        response = rq_enableSet(self.param,sid="adb",camera_id=getConf('data', 'camera_id1'),enable=True)
        print response 
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
       
    def test_c(self):
        u'''wrong camera_id  , correct sid enable'''
        response = rq_enableSet(self.param,sid=getConf("data","sid"),camera_id="hjjk",enable=True)
        print response 
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')
       
    def test_d(self):
        u''' correct sid camera_id , no enable'''
        response = rq_enableSet(self.param,sid=getConf("data","sid"),camera_id=getConf('data', 'camera_id1'))
        print response 
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_enableSet()
    a.test_d()

