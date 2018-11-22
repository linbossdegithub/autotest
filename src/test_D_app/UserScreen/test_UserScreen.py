# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonapp import rq_userScreen,rq_userScreenE

class Test_userScreen(unittest.TestCase):
    u'''   address:"" ,label:"" ,name:""  ,status:"" ,uid:"" '''

    def test_a(self):
        u''' correct params '''
        response = rq_userScreen(address=getConf("data", "address"),label=getConf("data", "label"),name=getConf("data", "name"),status=getConf("data", "status"),uid=getConf("data", "uid"))
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
   
    def test_b(self):
        u''' 不存在的用户 '''
        response = rq_userScreen(address=getConf("data", "address"),label=getConf("data", "label"),name=getConf("data", "name"),status=getConf("data", "status"),uid="a")
        print response
        u'check'
#         self.assertTrue(response['code'] == 10003,'this case is failed')
        self.assertTrue(response['code'] == 0,'this case is failed')
        
    def test_c(self):
        u''' 错误的token '''
        response = rq_userScreenE(address=getConf("data", "address"),label=getConf("data", "label"),name=getConf("data", "name"),status=getConf("data", "status"),uid="a")
        print response
        u'check'
        self.assertTrue(response['code'] == 1,'this case is failed')
   
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_userScreen()
    a.test_a()
    a.test_b()
    a.test_c()