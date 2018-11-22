# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonwechat import rq_addImg

class Test_AddImg(unittest.TestCase):
    u''' jpg'''

    def test_a(self):
        u''' correct params '''
        response = rq_addImg(a='g' )
        print response
        u'check'
        self.assertTrue(response['status'] == 100001, 'this case is failed')
    def runTest(self):
        pass
if __name__ == '__main__':
    a = Test_AddImg()
    a.test_a()

