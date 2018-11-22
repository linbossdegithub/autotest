# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonwechat import rq_detail

class Test_Detail(unittest.TestCase):
    u''' node, sid , language , page  openid'''

    def test_a(self):
        u''' correct params '''
        response = rq_detail(node='cn',sid=getConf('data','sid'),language=getConf('data','language'),page = '1', openid=getConf('data','openid'))                                 
        print response
        u'check'
        self.assertTrue(response== response, 'this case is failed')
    def runTest(self):
        pass
if __name__ == '__main__':
    a = Test_Detail()
    a.test_a()

