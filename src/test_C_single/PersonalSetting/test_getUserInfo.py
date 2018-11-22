#coding=utf-8
import unittest
from common.common import rq_getUserInfo
from parametrizedTestCase import ParametrizedTestCase


class Test_getUserInfo(ParametrizedTestCase):
    def test_a(self):
        response = rq_getUserInfo(self.param)
        print response 
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def runTest(self):
        pass

if __name__ == "__main__":
    a = Test_getUserInfo()
    a.test_a()