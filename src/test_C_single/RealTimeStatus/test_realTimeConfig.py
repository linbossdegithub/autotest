#coding=utf-8
import unittest
from common.common import rq_realTimeConfig
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf

class Test_realTimeConfig(ParametrizedTestCase):
    u''' params sid '''
    def test_a(self):
        u''' correct sid '''
        response = rq_realTimeConfig(self.param,sid=getConf('data', 'sid'))
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
    def test_b(self):
        u''' no sid '''
        response = rq_realTimeConfig(self.param,)
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')
        
        
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_realTimeConfig()
    a.test_a()
    a.test_b()
