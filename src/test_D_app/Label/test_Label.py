# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonapp import rq_label,rq_labelE

class Test_Label(unittest.TestCase):
    u'''   uid:""  '''

    def test_a(self):
        u''' correct params '''
        response = rq_label(uid=getConf("data", "uid"))
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
    def test_b(self):
        u''' 参数错误'''
        response = rq_label(uid="")
        print response
        u'check'
        self.assertTrue(response['code'] == 10001 ,'this case is failed')
    def test_c(self):
        u''' 错误token'''
        response = rq_labelE(uid="")
        print response
        u'check'
        self.assertTrue(response['code'] == 1 ,'this case is failed')
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_Label()
    a.test_a()
    a.test_b()
    a.test_c()