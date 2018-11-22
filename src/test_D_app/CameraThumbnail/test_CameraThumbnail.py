# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonapp import rq_cameraThumbnail

class Test_CameraThumbnail(unittest.TestCase):
    u''' sids'''

    def test_a(self):
        u''' correct params '''
        li = [getConf('data','sid')]
        response = rq_cameraThumbnail(height=400,width=400,sid=li)
        print response
        u'check'
        self.assertTrue(response['code'] == 0, 'this case is failed')

    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_CameraThumbnail()
    a.test_a()
#     a.test_b()

