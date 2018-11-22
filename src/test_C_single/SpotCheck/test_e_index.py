#coding=utf-8
import time
import unittest

from common.common import rq_index
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_index(ParametrizedTestCase):
    u''' id '''
    def test_a(self):
        u''' correct sid '''
        
        print getConf('data','sid')
        response = rq_index(self.param,id = getConf('data','sid'))
        
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_b(self):
        u''' wrong sid '''
        response = rq_index(self.param,id = "abd")
        print response
        u'check'
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_index()
    a.test_a()
    a.test_b()
        
    
