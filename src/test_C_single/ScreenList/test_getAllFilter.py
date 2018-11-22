#coding=utf-8
import unittest
from common.common import rq_getAllFilter
from parametrizedTestCase import ParametrizedTestCase


class Test_getAllFilter(ParametrizedTestCase):
    u''' no'''
    def test_a(self):
        u''' correct params '''
        response = rq_getAllFilter(self.param)
        print response
        u'check'
        self.assertTrue(response['status']==100000 and response['data']>0, 'this case is failed')
        
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_getAllFilter()
    a.test_a()
    

