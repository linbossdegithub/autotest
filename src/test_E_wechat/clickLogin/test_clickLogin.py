# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonwechat import rq_clickLogin

class Test_clickLogin(unittest.TestCase):
    u''' jpg'''

    def test_a(self):
        u''' correct params '''
        response = rq_clickLogin()
        print response
        u'check'
        self.assertTrue(response == response, 'this case is failed')
    def runTest(self):
        pass
if __name__ == '__main__':
    a = Test_clickLogin()
    a.test_a()

