# coding=utf-8
import unittest

from tools.tools import getConf, create_phone

from common.commonapp import rq_checkPhone

class Test_CheckPhone(unittest.TestCase):
    u''' countryCode:"",phone:""   '''

    def test_a(self):
        u''' correct params '''

        if getConf('data','phone'):
            telephone = getConf('data','phone')
            print telephone
            response = rq_checkPhone(countryCode=getConf("data", "countryCode"), phone=getConf("data", "phone"))
            print response
            u''' check '''
            self.assertTrue(response['code'] == 0, 'this case is failed')
        else:
            telephone = create_phone()
            response = rq_checkPhone(countryCode=getConf("data", "countryCode"), phone=telephone)
            print response
            u''' check '''
            self.assertTrue(response['code'] == 0, 'this case is failed')

    # def test_b(self):
    #     u'''  已注册 phone'''
    #     response = rq_checkPhone(countryCode="86",phone="18294447754")
    #     print response
    #     u'check'
    #     self.assertTrue(response['code'] == 10006 ,'this case is failed')
        
    def test_c(self):
        u'''   wrong phone'''
        response = rq_checkPhone(countryCode="86",phone="qwq")
        print response
        u'check'
        self.assertTrue(response['code'] == 10001 ,'this case is failed')   
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_CheckPhone()
    a.test_a()
    a.test_b()
    a.test_c()   