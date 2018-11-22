#coding=utf-8
import unittest
from common.common import rq_nameList
from parametrizedTestCase import ParametrizedTestCase


class Test_nameList (ParametrizedTestCase):
    u''' none'''
        
    def test_a(self):
        response = rq_nameList (self.param)
        print response
        u'check'
        self.assertTrue(response['status']==100000 and len(response['data'])>0, 'this case is failed')
        
        
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_nameList ()
    a.test_a()
         
    

