# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonapp import rq_detect,rq_detectE

class Test_Detect(unittest.TestCase):
    u'''   sid:""  '''

    def test_a(self):
        u''' correct params '''
        response = rq_detect(sid=getConf("data","sid"))
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
    def test_b(self):
        u''' 不存在的屏体'''
        response = rq_detect(sid="111111111111111")
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
#         self.assertTrue(response['code'] == 10002 ,'this case is failed')
    def test_c(self):
        u''' 参数错误'''
        response = rq_detect(sid="re3")
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
#         self.assertTrue(response['code'] == 10001 ,'this case is failed')
    def test_d(self):
        u''' correct params '''
        response = rq_detectE(sid=getConf("data","sid"))
        print response
        u'check'
        self.assertTrue(response['code'] == 1,'this case is failed')
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_Detect()
    a.test_a()
    a.test_b()
    a.test_c()
    a.test_d()