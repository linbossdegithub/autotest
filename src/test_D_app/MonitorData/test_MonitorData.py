# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonapp import rq_monitorData,rq_monitorDataE

class Test_monitorData(unittest.TestCase):
    u'''   sid:""   '''

    def test_a(self):
        u''' correct params '''
        response = rq_monitorData(sid=getConf("data", "sid"))
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
   
    def test_b(self):
        u''' 参数错误 '''
        response = rq_monitorData(sid="w")
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
#         self.assertTrue(response['code'] == 10001,'this case is failed')
   
    def test_c(self):
        u''' 不存在的屏体'''
        response = rq_monitorData(sid="112000000")
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
#         self.assertTrue(response['code'] == 10002,'this case is failed')
    def test_e(self):
        u''' 错误的token'''
        response = rq_monitorDataE(sid="1120")
        print response
        u'check'
        self.assertTrue(response['code'] == 1 ,'this case is failed')
#         self.assertTrue(response['code'] == 10002,'this case is failed')   
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_monitorData()
    a.test_a()
    a.test_b()
    a.test_c()
    a.test_e()