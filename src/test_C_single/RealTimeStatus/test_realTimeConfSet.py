#coding=utf-8
import unittest
from common.common import rq_realTimeConfSet
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf

class Test_realTimeConfSet(ParametrizedTestCase):
    u''' params  sids:["4354"]  switch:1  time:300  type:2 '''
    def test_a(self):
        u''' correct params '''
        
        response = rq_realTimeConfSet(self.param,sids=[getConf('data', 'sid')],switch=1,time=300,type=2)
        print response
        u''' check '''
        self.assertTrue(response['status']==100000 and response['data']['code']==1, 'this case is failed')
        
    def test_b(self):
        u''' wrong sid '''
        response = rq_realTimeConfSet(self.param,sids=[getConf('data', 'sid'),123],switch=1,time=300,type=2)
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')

        
        
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_realTimeConfSet()
    a.test_a()
    a.test_b()
