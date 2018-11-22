#coding=utf-8
import unittest

from common.common import rq_add
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import setConf


class Test_add(ParametrizedTestCase):
    u''' params name'''
    def test_a(self):
        u''' name=$adc '''
        response = rq_add(self.param,name="$abc")
        print response
        setConf('data','tem_id',response['data']['tem_id'])
        setConf('data','tem_spot_name',"$abc")
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
        
    def test_b(self):
        u''' repeat name '''
        response = rq_add(self.param,name="$abc")
        print response
        u'check'
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def test_c(self):
        u''' no name '''
        response = rq_add(self.param,)
        print response
        u'check'
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_add()
    a.test_a()
#     a.test_b()
#     a.test_c()
        
    
