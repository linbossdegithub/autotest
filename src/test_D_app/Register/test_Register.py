# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonapp import rq_register

class Test_register(unittest.TestCase):
    u'''   authCode:"" ,countryCode:"" ,email:"" ,language:"" ,password:"" ,phone:""   ,username:"" '''

    def test_a(self):
        u''' correct params '''
        response = rq_register(sid=getConf("data", "sid"))
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
   
    def test_b(self):
        u''' 参数错误 '''
        response = rq_register(sid="w")
        print response
        u'check'
        self.assertTrue(response['code'] == 10001,'this case is failed')
   
    def test_c(self):
        u''' 不存在的屏体'''
        response = rq_register(sid="1120")
        print response
        u'check'
        self.assertTrue(response['code'] == 10002,'this case is failed')
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_register()
    a.test_a()
    a.test_b()
    a.test_c()