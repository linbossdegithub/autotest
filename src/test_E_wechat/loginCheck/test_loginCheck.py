# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonwechat import rq_loginCheck

class Test_loginCheck(unittest.TestCase):
    u''' jpg'''

    def test_a(self):
        u''' "node":"us","username":"linhuajian","password":"123456","openid":"olKdEwH__QGy8I_i1Yoh8347pqfA"'''
        response = rq_loginCheck(node='us' ,username='linhuajian',password='123456' ,openid='olKdEwH__QGy8I_i1Yoh8347pqfA', )
        print response
        u'check'
        self.assertTrue(response['status'] == 100001, 'this case is failed')
    def runTest(self):
        pass
if __name__ == '__main__':
    a = Test_loginCheck()
    a.test_a()

