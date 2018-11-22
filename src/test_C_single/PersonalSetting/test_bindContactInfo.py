#coding=utf-8
import unittest
from common.common import rq_bindContactInfo
from parametrizedTestCase import ParametrizedTestCase


class Test_bindContactInfo(ParametrizedTestCase):
    u''' telephone: "17629228903", type: 1, verifyCode: "123456", countryCode: "0" '''
    u''' email: "nova_chenyf@126.com", type: 2, verifyCode: "123456" '''
    def test_a(self):
        response = rq_bindContactInfo(self.param,telephone="17629228903", type=1, verifyCode="123456", countryCode="0")
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def test_b(self):
        response = rq_bindContactInfo(self.param,email="nova_chenyf@126.com", type=2, verifyCode="123456")
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')
    def runTest(self):  
        pass
        
if __name__ == '__main__':
    a = Test_bindContactInfo()
    a.test_a()
    a.test_b()
    
    
    