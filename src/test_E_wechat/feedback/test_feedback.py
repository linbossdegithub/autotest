# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonwechat import rq_feedback
class Test_Feedback(unittest.TestCase):
    u''' '''

    def test_a(self):
        u''' correct params '''
        response = rq_feedback()
        print response
        u'check'
        self.assertTrue(response==response , 'this case is failed')
    def runTest(self):
        pass
if __name__ == '__main__':
    a = Test_Feedback()
    a.test_a()

