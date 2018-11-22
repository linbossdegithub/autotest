# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonapp import rq_Image,rq_ImageE

class Test_Image(unittest.TestCase):
    u'''   sid:""  '''

    def test_a(self):
        u''' correct params '''
        response = rq_Image(sid=[4394])
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
    def test_b(self):
        u''' 不存在的屏体'''
        response = rq_Image(sid=[8888])
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
#         self.assertTrue(response['code'] == 10002 ,'this case is failed')
    def test_c(self):
        u''' 错误token '''
        response = rq_ImageE(sid=[4394])
        print response
        u'check'
        self.assertTrue(response['code'] == 1 ,'this case is failed')  
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_Image()
    a.test_a()
    a.test_b()
    a.test_c()