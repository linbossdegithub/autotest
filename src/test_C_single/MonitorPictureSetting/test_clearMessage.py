#coding=utf-8
import unittest
from common.common import rq_clearmessages
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_clearMessages(ParametrizedTestCase):
    u''' params sid '''
    def test_a(self):
        u''' correct sid '''
        response = rq_clearmessages(self.param,sid=getConf('data','sid'))
        print response 
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_b(self):
        u''' wrong sid '''
        response = rq_clearmessages(self.param,sid="000000")
        print response 
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_c(self):
        u''' no sid '''
        response = rq_clearmessages(self.param)
        print response 
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def runTest(self):
        pass
       
        
        
