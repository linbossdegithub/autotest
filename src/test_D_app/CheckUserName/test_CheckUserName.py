# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonapp import rq_checkUserName

class Test_CheckUserName(unittest.TestCase):
    u''' username:"" '''

    def test_a(self):
        u''' correct params '''
        response = rq_checkUserName(username="dada")
        print response
        u'check'
        self.assertTrue(response['code'] == 0 ,'this case is failed')
    def test_b(self):
        u'''  已注册 username'''
        response = rq_checkUserName(username=getConf("constant", "user"))
        print response
        u'check'
        self.assertTrue(response['code'] == 10004 ,'this case is failed')
        
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_CheckUserName()
    a.test_a()
    a.test_b()