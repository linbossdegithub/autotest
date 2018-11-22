#coding=utf-8
import unittest
from common.common import rq_getInfoBySid
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_getInfoBySid(ParametrizedTestCase):
    u''' id '''
    def test_a(self):
        u''' correct sid '''
        response = rq_getInfoBySid(self.param,id = getConf('data','sid'))
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_b(self):
        u''' wrong sid '''
        response = rq_getInfoBySid(self.param,id = "abd")
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_getInfoBySid()
    a.test_a()
    a.test_b()
        
    