#coding=utf-8
import unittest
from common.common import rq_saveBaseInfo
from parametrizedTestCase import ParametrizedTestCase


class Test_saveBaseInfo(ParametrizedTestCase):
    u''' params nick  emailLanguage '''
       
    
    def test_a(self):
        u'''wrong emailLanguage=10'''
        response = rq_saveBaseInfo(self.param,nick="chen",emailLanguage="10")
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
    def test_b(self):
        u'''nick=/#$%'''
        response = rq_saveBaseInfo(self.param,nick="/#$%",emailLanguage="1")
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')
    def test_c(self):
        u'''no  nick'''
        response = rq_saveBaseInfo(self.param,emailLanguage="1")
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')
    def test_d(self):
        u'''no  emailLanguage'''
        response = rq_saveBaseInfo(self.param,nick="chen")
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_e(self):
        u'''correct nick emailLanguage'''
        response = rq_saveBaseInfo(self.param,nick="chen",emailLanguage="1")
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def runTest(self):
        pass
    
if __name__ == "__main__":
    a = Test_saveBaseInfo()
    a.test_d()

