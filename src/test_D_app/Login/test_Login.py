# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonapp import rq_login,rq_rlogin

class Test_Login(unittest.TestCase):
    u'''   password:""  , username:""   '''

    def test_a(self):
        u''' correct params '''
        response = rq_rlogin(password=getConf("constant", "password"),username=getConf("constant", "user"))
        print response
        u'check'
#         self.assertTrue(response['code'] == 0 and response["uid"]==2548 ,'this case is failed')
        self.assertTrue(response['code'] == 0 ,'this case is failed')
    def test_b(self):
        u''' 参数错误 '''
        response = rq_login(password="",username="w")
        print response
        u'check'
        self.assertTrue(response['code'] == 10001,'this case is failed')
   
    def test_c(self):
        u''' 登录失败，用户名或密码错误'''
        response = rq_login(password="w",username="w")
        print response
        u'check'
        self.assertTrue(response['code'] == 10005,'this case is failed')
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_Login()
    a.test_a()
    a.test_b()
    a.test_c()