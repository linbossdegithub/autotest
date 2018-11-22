#coding=utf-8
import unittest
from common.common import rq_list
from parametrizedTestCase import ParametrizedTestCase


class Test_list (ParametrizedTestCase):
    u''' params currentPage: 1  orderName:   orderType:    pageSize: 10'''
        
    def test_a(self):
        u''' correct params '''
        response = rq_list (self.param,currentPage=1, pageSize=10)
        print response
        u'check'
        self.assertTrue(response['status']==100000 and len(response['data'])>0, 'this case is failed')
        
    def test_b(self):
        u''' no params '''
        response = rq_list (self.param,)
        print response
        u'check'
        self.assertTrue(response['status']==100000 and len(response['data'])>0, 'this case is failed')
        
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_list ()
    a.test_a()
    a.test_b()
         
    

