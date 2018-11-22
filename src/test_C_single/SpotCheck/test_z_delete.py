#coding=utf-8
import unittest

from common.common import rq_delete
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_delete(ParametrizedTestCase):
    u''' params {idArray: [320]}'''
        
    def test_a(self):
        u''' correct params '''
        li = [getConf('data', 'tem_id')]
        response = rq_delete(self.param,idArray=li)
        print response
        u'check'
        self.assertTrue(response['status']==100000 and response['data']==1, 'this case is failed')
        
        
    def test_c(self):
        u''' no id Array '''
        response = rq_delete(self.param,)
        print response
        u'check'
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def test_d(self):
        u''' wrong idArray '''
        response = rq_delete(self.param,idArray=['a','b'])
        print "idArray=['a','b']"
        print response
        u'check'
        self.assertTrue(response['status']==100000 and response['data']==0, 'this case is failed')
        
    def runTest(self):
        pass 
        

    
