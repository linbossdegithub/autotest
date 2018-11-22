#coding=utf-8
from common.common import rq_deleteScreen, rq_delete, rq_getScreenList
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf, setConf


class Test_clear(ParametrizedTestCase):
    def test_a(self):
        u'''清理之前注册的屏体'''
        r = self.param
        sid = ''
        result = rq_getScreenList(r,PageSize='100')
        print result
        for li in result['data']['ScreenList']:
            if li['ScreenName'] == getConf('constant', 'led_name') or li['ScreenName'] == getConf('websocketdata', 'websocketName'):
                sid = li['Sid']
                if sid :
                    print sid
                    result = rq_deleteScreen(self.param, sids=[sid])
                    self.assertTrue(result['status']==100000)
                else:
                    print 'no this screen'

    def test_b(self):
        u'''清理之前增加的模板'''
        try:
            rq_delete(self.param,idArray=[getConf('data', 'tem_id')])
        except:
            print 'spotTem has been deleted'

