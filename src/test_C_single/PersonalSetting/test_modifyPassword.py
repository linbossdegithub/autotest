#coding=utf-8
import unittest
from common.common import rq_modifyPassword
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf

class Test_modifyPassword(ParametrizedTestCase):
    u''' params oldPwd  newPwd  confirmPwd ''' 
    def test_a(self):
        u''' correct params '''
        response = rq_modifyPassword(self.param,oldPwd=getConf('constant','password'),newPwd=getConf('constant','password'),confirmPwd=getConf('constant','password'))
        print response 
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_b(self):
        u''' wrong oldPwd '''
        response = rq_modifyPassword(self.param,oldPwd='abc',newPwd=getConf('constant','password'),confirmPwd=getConf('constant','password'))
        print response 
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    # def test_c(self):
    #     u''' wrong confirmPwd '''
    #     response = rq_modifyPassword(self.param,oldPwd=getConf('constant','password'),newPwd=getConf('constant','password'),confirmPwd='abc')
    #     print response
    #     u''' check '''
#         self.assertTrue(response['status']==100001, 'this case is failed')
        
    def test_d(self):
        u''' no  oldPwd'''
        response = rq_modifyPassword(self.param,newPwd=getConf('constant','password'),confirmPwd=getConf('constant','password'))
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_modifyPassword()
#     a.test_a()
#     a.test_b()
    a.test_c()
    a.test_d()
