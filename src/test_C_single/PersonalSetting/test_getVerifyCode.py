#coding=utf-8

import unittest

from parametrizedTestCase import ParametrizedTestCase
from tools.tools import create_phone
from common.common import rq_getVerifyCode
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import create_phone, getConf


class Test_getVerifyCode(ParametrizedTestCase):
    u''' telephone or email, type: 1 or 2, countryCode: "0" '''
    # def test_a(self):
    #     u''' telephone=17629228904 '''
    #     response = rq_getVerifyCode(self.param,telephone='17629228904',type=1, countryCode="0")
    #     print response
    #     u''' check '''
    #     self.assertTrue(response['status']==100001, 'this case is failed')
        
    def test_b(self):
        u''' send verifycode to your phone or random phone '''
        if getConf('data','phone'):
            telephone = getConf('data','phone')
            response = rq_getVerifyCode(self.param, telephone=telephone, type=1, countryCode="0")
            print response
            u''' check '''
            self.assertTrue(response['status'] == 100000, 'this case is failed')
        else:
            telephone = create_phone()
            response = rq_getVerifyCode(self.param,telephone=telephone,type=1, countryCode="0")
            print response
            u''' check '''
            self.assertTrue(response['status']==100000, 'this case is failed')
        
    # def test_c(self):
    #     u''' email=nova_chenyf@126.com '''
    #     response = rq_getVerifyCode(self.param,email='nova_chenyf@126.com',type=2)
    #     print response
    #     u''' check '''
    #     self.assertTrue(response['status']==100001, 'this case is failed')
        
    def test_d(self):
        u''' send verifycode to your email'''
        email = getConf('data', 'email')
        response = rq_getVerifyCode(self.param,email=email,type=2)
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
    
    def runTest(self):
        pass
    
