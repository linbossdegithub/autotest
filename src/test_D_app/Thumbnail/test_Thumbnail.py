# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonapp import rq_thumbnail,rq_thumbnailE

class Test_thumbnail(unittest.TestCase):
    u'''   sid:""  '''

    def test_a(self):
        u''' correct params '''
        response = rq_thumbnail(sid=[4394])
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
   
    def test_b(self):
        u''' 错误token '''
        response = rq_thumbnailE(sid=getConf("data", "sid"))
        print response
        u'check'
        self.assertTrue(response['code'] == 1 ,'this case is failed')
    
#     def test_c(self):
#         u''' correct params '''
#         response = rq_thumbnail(sid=getConf("data", "sid"))
#         print response
#         u'check'
#         self.assertTrue(response['code'] == 0 ,'this case is failed')
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_thumbnail()
    a.test_a()
    a.test_b()
#     a.test_c()