#coding=utf-8
import unittest
from common.common import rq_nameSet
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_nameSet(ParametrizedTestCase):
    u'''params camera_id name '''
       
    def test_a(self):
        u'''correct camera_id name'''
        response = rq_nameSet(self.param,camera_id=getConf('data','camera_id1'),name="camera123")
        print response
        u'''check'''
        self.assertTrue(response['status']==100000, 'this case is failed')
       
    def test_b(self):
        u'''wrong camera_id '''
        response = rq_nameSet(self.param,camera_id='123',name="camera123")
        print response
        u'''check'''
        self.assertTrue(response['status']==100001, 'this case is failed')
       
    def test_c(self):
        u'''name = 123 '''
        response = rq_nameSet(self.param,camera_id=getConf('data','camera_id1'),name=123)
        print response
        u'''check'''
        self.assertTrue(response['status']==100000, 'this case is failed')
       
    def test_d(self):
        u'''name = @#$ '''
        response = rq_nameSet(self.param,camera_id=getConf('data','camera_id1'),name="@#$")
        print response
        u'''check'''
        self.assertTrue(response['status']==100000, 'this case is failed')
       
    def test_e(self):
        u'''name = / '''
        response = rq_nameSet(self.param,camera_id=getConf('data','camera_id1'),name="/")
        print response
        u'''check'''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_f(self):
        u'''correct camera_id name'''
        response = rq_nameSet(self.param,camera_id=getConf('data','camera_id1'),name="camera1")
        print response
        u'''check'''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_nameSet()
    a.test_e()

