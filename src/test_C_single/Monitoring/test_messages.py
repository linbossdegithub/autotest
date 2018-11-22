#coding=utf-8
import unittest

from common.common import rq_messages
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import  getConf


class Test_messages(ParametrizedTestCase):
    
    u'''参数：sid  ''' 
    def test_a(self):
        u'''正确的sid'''
        sid = getConf("data","sid")
        response = rq_messages(self.param,sid=sid)
        print response
        u''' check'''
        self.assertTrue(response["status"]==100000,u"this case is failed")
    
    def test_b(self):
        u'''错误的sid'''
        response = rq_messages(self.param,sid="0")
        u''' check'''
        print response
        self.assertTrue(response["status"]==100000,u"this case is failed")
        
    def test_c(self):
        u'''错误的sid'''
        response = rq_messages(self.param,sid=4329)
        u''' check'''
        print response
        self.assertTrue(response["status"]==100000,u"this case is failed")

    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_messages()
    a.test_a()
    a.test_b()
    a.test_c()
