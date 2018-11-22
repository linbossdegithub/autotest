# coding=utf-8
import unittest

from tools.tools import getConf, create_phone

from common.commonapp import rq_send

class Test_send(unittest.TestCase):
    u'''   phone:""  countrycode:"" ,language:""  '''
    global phone
    phone= create_phone()
    def test_a(self):
        u''' correct params '''
        response = rq_send(countryCode=getConf("data", "countryCode"),phone=phone,language=getConf("data", "language"))
 
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
    
    def test_b(self):
        u''' 频繁发送验证码 '''
        response = rq_send(countryCode=getConf("data", "countryCode"),language=getConf("data", "language"),phone=phone)
        print response
        u'check'
        self.assertTrue(response['code'] ==10010 ,'this case is failed')
    
    def test_c(self):
        u''' 验证码发送失败'''
        response = rq_send(countryCode="86",language="zh-cn",phone="182944")
        print response
        u'check'
        self.assertTrue(response['code'] ==10011 ,'this case is failed')
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_send()
    # a.test_a()
    # a.test_b()
    a.test_c()