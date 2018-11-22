#coding=utf-8
import unittest

from common.common import rq_screens
from parametrizedTestCase import ParametrizedTestCase


class Test_screens(ParametrizedTestCase):
    u''' 无参数'''
    def test_a(self):
        u'''不传参数'''
        response = rq_screens(self.param)
        print response
        u''' check'''
        self.assertTrue(response["status"]==100000,u"this case is failed")
        
    def test_b(self):
        u'''传参'''
        response = rq_screens(self.param,sid="123")
        print response
        u''' check'''
        self.assertTrue(response["status"]==100000,u"this case is failed")
        
    def runTest(self):
        pass
    
if __name__ == "__main__":
    a = Test_screens()
    a.test_b()
    a.test_a()