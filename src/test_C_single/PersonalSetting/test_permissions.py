#coding=utf-8
import unittest
from common.common import rq_permissions
from parametrizedTestCase import ParametrizedTestCase


class Test_permissions(ParametrizedTestCase):
    def test_a(self):
        response = rq_permissions(self.param)
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case if failed')
    
    def runTest(self):
        pass
    
    
