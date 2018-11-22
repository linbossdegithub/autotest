#coding=utf-8
import unittest
from common.common import rq_getInfoById
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import  setConf, getConf


class Test_getInfoById (ParametrizedTestCase):
    u''' params id'''
    def test_a(self):
        u''' correct id '''
        response = rq_getInfoById (self.param,id=getConf('data','tem_id'))
        print response
        u'check'
        self.assertTrue(response['status']==100000 and len(response['data'])!=0, 'this case is failed')
        
        
    def test_b(self):
        u''' wrong id '''
        response = rq_getInfoById (self.param,id="$abc")
        print response
        u'check'
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def test_c(self):
        u''' no id '''
        response = rq_getInfoById (self.param,)
        print response
        u'check'
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_getInfoById ()
    a.test_a()
    a.test_b()
    a.test_c()
         
    

