# coding=utf-8
from flask import json

from common.common import rq_getShowNotice
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf, getHeaders


class Test_Others(ParametrizedTestCase):
    def test_a(self):
        u'''验证首页getShowNotice接口'''
        response = rq_getShowNotice(self.param)
        print response
        u''' check '''
        self.assertTrue(response["status"] == 100000 , "this case is failed")

    def test_b(self):
        u'''建议反馈接口'''
        url = getConf("constant", "url") + '/new/backend/feedback/create'
        headers = getHeaders()
        data = {'type': 1, 'title': 'abc', 'content': 'adb', 'email': 'chen@qq.com', 'country_code': '86', 'phone': ''}
        response = self.param.request(method='post',url=url, headers=headers, data=data)
        self.assertTrue(json.loads(response.text)['status']==100000,'this case is failed')


    def runTest(self):
        pass


if __name__ == "__main__":
    a = Test_cameras()
    a.test_a()
    a.test_b()
    a.test_c()

