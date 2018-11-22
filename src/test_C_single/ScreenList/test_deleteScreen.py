# coding=utf-8
import unittest

from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf

from common.common import rq_deleteScreen


class Test_deleteScreen(ParametrizedTestCase):
    u''' sids'''

    def test_a(self):
        u''' correct params '''
        li = [getConf('data','sid')]
        response = rq_deleteScreen(self.param,sids=li)
        print response
        u'check'
        self.assertTrue(response['status'] == 100000 and response['data']['code'] == 1, 'this case is failed')

    def runTest(self):
        pass


if __name__ == '__main__':
    a = Test_deleteScreen()
    a.test_a()



