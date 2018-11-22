# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonwechat import rq_wechatCreate
#{"openid":"olKdEwH__QGy8I_i1Yoh8347pqfA","type":"1","title":"界面太丑","content":"系统页面不美观","email":"","phone":"","country_code":"","files":[]}

class Test_WechatCreate(unittest.TestCase):
    u''' sid'''

    def test_a(self):
        u''' correct params '''
        li = [getConf('data','sid')]
        response = rq_wechatCreate()(sid=li)
        print response
        u'check'
        self.assertTrue(response['code'] == 0 , 'this case is failed')
    def runTest(self):
        pass
if __name__ == '__main__':
    a = Test_WechatCreate()
    a.test_a()

